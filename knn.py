from sklearn import datasets,preprocessing
import numpy as np
from sklearn.model_selection import train_test_split

#Step1: Import the required data and check the features.
iris=load_iris()
print("Iris data")
print(iris)
print("\n")
print("Iris feature_names")
print("\n")
print(iris.feature_names)
print("\n")
print("integers representing features(0=setosa,1=versicolor,2=virginica)")
print("\n")
print(iris.target)
print("\n")
print("3classes of target")
print("\n")
#3classes of target
print(iris.target_names)
print("\n")
#we have a total of 150 observations and 4 features
print("total of 150 observations and 4 features")
print("\n")
print(iris.data.shape)
print("\n")

#Step2: Split the data and Train the Model.
X, y = iris.data[:, :], iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify = y, random_state = 0, train_size = 0.7)
#shape of train and test objects
print("shape of train and test objects")
print("\n")

print(X_train.shape)
print(X_test.shape)
print("\n")
#shape of new y objects
print("shape of new y objects")
print("\n")
print(y_train.shape)
print(y_test.shape)
print("\n")
print("training data before preprocessing")
print(X_train)
print("\n")
scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
print("display scaled data")
print("\n")
print(X_train)
print("\n")
X_test = scaler.transform(X_test)

#Step 3: Train the Model and Evaluate the model .

scores = []
k_range = range(1,15)
for k in k_range:

  knn = neighbors.KNeighborsClassifier(n_neighbors=k)
  knn.fit(X_train, y_train)
  y_pred = knn.predict(X_test)
  
  
print("Prediction of Species: {}".format(y_pred))  
print("Accuracy score")
print(accuracy_score(y_test, y_pred))
print("Confusion matrix")
print(confusion_matrix(y_test, y_pred))
print("Classification Report")
print(classification_report(y_test, y_pred))






