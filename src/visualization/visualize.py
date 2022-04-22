import seaborn as sns
from sklearn import metrics
from sklearn.metrics import confusion_matrix


def plot_confusion_matrix(y_test, y_pred):
    """
    returns a plot of the confusion matrix

    Args:
        y_test: the target data from the test
        y_pred: the predicted label from the model

    Returns:
        A visualization figure.
    """
    matrix = confusion_matrix(y_test, y_pred)
    sns.heatmap(matrix, annot=True, cmap='PuBuGn_r', fmt='g')


def get_model_evaluation(y_test, y_pred):
    """
      Args:
          y_test: the target data from the test
          y_pred: the predicted label from the model

      Returns:
          an evaluation results as string
      """
    accuracy = metrics.accuracy_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    f1score = metrics.f1_score(y_test, y_pred)
    classification_report = metrics.classification_report(y_test, y_pred)

    print(
        f"Accuracy = {accuracy} \n Recall = {recall} \n Percision = {precision} \n f1_score = {f1score}\n Classification report: {classification_report}\n")


