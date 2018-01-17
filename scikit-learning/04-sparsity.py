# -*- coding:utf-8 -*-

import numpy as np
from sklearn import datasets
from sklearn import linear_model

diabetes = datasets.load_diabetes()
diabetes_X_train = diabetes.data[:-20]
diabetes_X_test = diabetes.data[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

alphas = np.logspace(-4,-1,6)

regr = linear_model.Lasso()
scores = [regr.set_params(alpha = alpha).fit(diabetes_X_train,
            diabetes_y_train).score(diabetes_X_test,
            diabetes_y_test) for alpha in alphas]

best_alpha = alphas[scores.index(max(scores))]
regr.alpha = best_alpha

results = regr.fit(diabetes_X_train,diabetes_y_train)

print(results)
print(regr.coef_)