
import matplotlib.pyplot as plt
from sklearn import linear_model

regr = linear_model.LinearRegression()


print(f'성별을 입력하세요 남자 1, 여자 2 :')
sex = input()

if sex==1:
    X = [[168],[166],[173],[165],[177],[163],[178],[172]]
    y = [65,61,68,63,68,61,76,67]
else:
    X = [[163],[162],[171],[162],[164],[162],[158],[173]]
    y = [55,51,59,53,61,56,44,57]

regr.fit(X,y)

plt.scatter(X, y, color='blue', marker='D')

y_pred = regr.predict(X)

plt.plot(X,y_pred,'r:')
