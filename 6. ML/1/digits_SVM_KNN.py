
from sklearn.svm import SVC

for K in ['linear', 'poly', 'rbf', 'sigmoid']:
    clf = SVC(kernel = K, C=1, gamma=0.001)
    clf.fit(Xtrain, Ytrain)
    ypred = clf.predict(Xtest)
    print 'For Kernel: ', K, ' the accuracy is: ', accuracy_score(Ytest, ypred)

from sklearn.neighbors import KNeighborsClassifier

for n in range(5, 26, 5):
    knn_obj = KNeighborsClassifier(n_neighbors=n)
    knn_obj.fit(Xtrain, Ytrain)
    ypred = knn_obj.predict(Xtest)
    print 'For {} neighbors, the accuracy is: {}'.format(n, 
                                                       accuracy_score(Ytest, ypred))