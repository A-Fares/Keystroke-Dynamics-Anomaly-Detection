from sklearn.ensemble import RandomForestClassifier
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from src.features.build_features import preprocessing_data
from src.visualization.visualize import plot_confusion_matrix, get_model_evaluation


def saveModel(model):
    with open(r"C:\Users\alaa\Desktop\Final CS\elg7186-project-group_project_-7\models\model_rf.sav", 'wb') as file:
        pickle.dump(model, file)


def training_model(df):
    # Split the data into training and test sets
    X, y = preprocessing_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    ## train the classifier
    random_forest_classifier = RandomForestClassifier(n_estimators=200, criterion='entropy', random_state=5)
    random_forest_classifier.fit(X_train, y_train)

    # plot_confusion_matrix(random_forest_classifier, X_test, y_test)
    # get_model_evaluation(random_forest_classifier, X_test, y_test)

    # Save the model
    saveModel(random_forest_classifier)
