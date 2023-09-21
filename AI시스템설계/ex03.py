
import matplotlib.pyplot as plt
from sklearn import linear_model

regr = linear_model.LinearRegression()

X = [[163],[179],[166],[169],[171]]
y = [54,63,57,56,58]

regr.fit(X,y)

plt.scatter(X, y, color='blue', marker='D')

y_pred = regr.predict(X)

plt.plot(X,y_pred,'r:')

unseen = [[167]]
result = regr.predict(unseen)
print('동윤이의 키카 {}cm 이므로 몸무게는 {}kg으로 추정됨'.format(unseen, result.round(1)))