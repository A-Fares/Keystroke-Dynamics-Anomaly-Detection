import pickle

import numpy as np

with open(r"E:\uOttawa\SecondTerm\AI for CS\elg7186-project-group_project_-7\models\model_rf.sav", 'rb') as pickle_file:
    model_rf = pickle.load(pickle_file)


    ## predict the new features
    def predict_model(msg):
        """
        returns a dataframe with all the columns created and populated

        Args:
            str : a value of the DNS data from the consumer

        Returns:
            A prediction of user type.
        """
        y_pred_propa = model_rf.predict_proba(msg)

        indexe = np.argmax(y_pred_propa, axis=-1)
        max_value = y_pred_propa[0][indexe]
        if max_value > 0.4:
            print("Genuine:", indexe)
            return "Genuine", indexe
        else:
            print("Imposter:", indexe)
            return "Imposter", indexe
