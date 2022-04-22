import pyHook
import pythoncom
import csv
from pathlib import Path
import json
import time 
import pandas as pd
from kafka import KafkaProducer

global userName
userFilePath = "Collecting_keyStorke.csv"

class KeyLogger:
    def __init__(self):
        self.enterPressed = False
        self.eventList = []
        self.isCaps = False
        #self.message = ""
        
    def keyDownEvent(self, event):
        if event.KeyID == 20 and self.isCaps == False:
            self.isCaps = True
        elif event.KeyID == 20 and self.isCaps == True:
            self.isCaps = False     
        if event.KeyID>= 48 and event.KeyID<=57:
            event.Ascii = event.KeyID
        if self.isCaps == True and event.Ascii>=97 and event.Ascii<=122:
            event.Ascii = event.KeyID
        self.storeEvent("Down", event) 
        return True
        # Fixes Requires Integer Bug (Got Nonetype)

    def keyUpEvent(self, event): 
        if event.KeyID>= 48 and event.KeyID<=57:
            event.Ascii = event.KeyID
        if self.isCaps == True and event.Ascii>=97 and event.Ascii<=122:
            event.Ascii = event.KeyID
        print(chr(event.Ascii),end='')
        self.storeEvent("Up", event)
        return True

    def mainLoop(self):
        while not self.enterPressed:
            pythoncom.PumpWaitingMessages()

    def storeEvent(self, activity, event):
        keystrokeTime = int(event.Time)
        self.eventList.append ((userName,event.Ascii,activity, int(keystrokeTime)))

        # Chosen to use Escape key (ESC) due to input using a similar method
        # Enter Key - KeyCode: 13 Ascii: 13 ScanCode: 28 - ESC = 27 @ Ascii
        if event.Ascii == 27:
            self.enterPressed = True
            userRecordData(self.eventList)

def userRecordData(eventList):
    print("\nouput")
    print(eventList)
    
    with open(userFilePath,'a',newline='\n') as f:
        writer = csv.writer(f)
        writer.writerows(eventList)
    f.close()   

def getUserName():
    global userName
    userName = input("Enter your Name: ")

def getKeyStroke():
    
    keyLogger = KeyLogger()
    hookManager = pyHook.HookManager()
    hookManager.KeyDown = keyLogger.keyDownEvent
    hookManager.KeyUp = keyLogger.keyUpEvent
    hookManager.HookKeyboard()

    keyLogger.mainLoop()
    # Unhooks the keyboard, no more data recorded, returns to menu
    hookManager.UnhookKeyboard()
    
getUserName()
print("Enter your text: ")
getKeyStroke()
#=====================================================================

data = pd.read_csv(userFilePath)
data.columns=['user', 'key', 'keyEvent', 'Time']
userList = data.user.unique()
keyList = data.key.unique()
df = pd.DataFrame(columns=['subject','key','H','UD','DD'])
for i in range(0, len(userList)):
    for j in range(0,len(keyList)):
        queryData = data.query("user=='" +userList[i]+ "' and key==" + str(keyList[j]) + " and key >=33 and key<=122")
        queryLen = len(queryData)
        finalData = {}
        if queryLen > 0:
            if(queryLen > 2):
                for k in range(0,queryLen,2):
                    finalData['subject'] = userList[i]
                    finalData['key'] = chr(keyList[j])
                    finalData['H'] = (int(queryData.iloc[k+1].Time) - int(queryData.iloc[k].Time))/1000
                    keyUpIndex = queryData.iloc[k+1].name
                    if(data.iloc[keyUpIndex + 1].user == userList[i]):
                        finalData['UD'] = (int(data.iloc[keyUpIndex+1].Time) - int(queryData.iloc[k+1].Time))/1000
                        finalData['DD'] = (int(data.iloc[keyUpIndex+1].Time) - int(queryData.iloc[k].Time))/1000
                    else:
                        finalData['UD'] =  finalData['H']
                        finalData['DD'] = finalData['H']
                    df = df.append(finalData,ignore_index=True )
            else:
                finalData['subject'] = userList[i]
                finalData['key'] = chr(keyList[j])
                finalData['H']= (int(queryData.query("keyEvent=='Up'").Time) - int( queryData.query("keyEvent=='Down'").Time))/1000
                keyUpIndex = queryData.query("keyEvent=='Up'").index[0]
                if(data.iloc[keyUpIndex + 1].user == userList[i]):
                        finalData['UD'] = (int(data.iloc[keyUpIndex+1].Time) - int( queryData.query("keyEvent=='Up'").Time))/1000
                        finalData['DD'] = (int(data.iloc[keyUpIndex+1].Time) - int( queryData.query("keyEvent=='Down'").Time))/1000
                else:
                    finalData['UD'] =  finalData['H']
                    finalData['DD'] =  finalData['H']
                df = df.append(finalData,ignore_index=True )
            
           
                
new_df=pd.DataFrame()
new_df.loc[0,"subject"]= df.iloc[0]["subject"]
for i,row in df.iterrows():
  new_df["H."+row['key']]=row["H"]
  new_df["UD."+row['key']]=row["UD"]
  new_df["DD."+row['key']]=row["DD"]
  new_df["return"]=.2
new_df = new_df.drop('subject', 1)
path = Path('KeyStrokeDistance.csv')

if path.is_file():
    new_df.to_csv('KeyStrokeDistance.csv', mode='a', header=False,index=False)
else:
    new_df.to_csv('KeyStrokeDistance.csv', mode='a', header=True,index=False)

f = open(userFilePath, 'w',newline='\n')
f.truncate()
f.close()


names=['H.period', 'DD.period.t', 'UD.period.t', 'H.t', 'DD.t.i',
       'UD.t.i', 'H.i', 'DD.i.e', 'UD.i.e', 'H.e', 'DD.e.five', 'UD.e.five',
       'H.five', 'DD.five.Shift.r', 'UD.five.Shift.r', 'H.Shift.r',
       'DD.Shift.r.o', 'UD.Shift.r.o', 'H.o', 'DD.o.a', 'UD.o.a', 'H.a',
       'DD.a.n', 'UD.a.n', 'H.n', 'DD.n.l', 'UD.n.l', 'H.l', 'DD.l.Return',
       'UD.l.Return', 'H.Return']


    
def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=json_serializer
    )

for i,row in new_df.iterrows():
    message = dict(zip(names, row.values))
    print(message)
    producer.send('read-test',message)
    time.sleep(3)