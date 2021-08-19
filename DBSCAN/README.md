# PCA-with-numpy
Introduce Principal Component Analysis(PCA) step by step with numpy: <br>
https://hackmd.io/@TKDOgu_kT3yWnqCyIxb3-Q/HyJr68TJt (traditional chinese)


## import PCA from PCA.py
```
import numpy as np
from DBSCAN import DBSCAN
```

## input of PCA
```
#sample 0 ~ 11
f1= np.array([1, 5, 1.5, 8, 1, 9, 7, 8.7, 2.3, 5.5, 7.7, 6.1])
f2 = np.array([2, 8, 1.8, 8, 0.6, 11, 10, 9.4, 4, 3, 8.8, 7.5])

plt.scatter(f1, f2)
plt.show()
```
![](https://i.imgur.com/xJqzU3P.png)


## 2-dim data
code:
```
data = np.array([f1, f2])
dbscan = DBSCAN(data, 3, 1)
dbscan.show_graph()
```
output: <br>
![](https://i.imgur.com/WOz2aDl.png)

## for more dim
code:
```
data = np.random.rand(3,10)*100
dbscan = DBSCAN(data, 50, 1)
print("It has " +str(dbscan.cluster_count)+ " cluster(s)")
dbscan.show()
```
output: <br>
```
It has 6 cluster(s)
Sample: [22.93015635  7.82619701  4.62407773] Cluster ID 1
Sample: [41.8956658  91.36418864 19.83055023] Cluster ID 2
Sample: [97.03254444 63.48855169 23.68614179] Cluster ID 3
Sample: [19.86966834 60.23624661 87.03766231] Cluster ID 4
Sample: [78.44046287 49.70500624 52.5996821 ] Cluster ID 3
Sample: [81.96498511 81.32456948 77.88320779] Cluster ID 3
Sample: [83.85706315 35.23914734 15.85233547] Cluster ID 3
Sample: [96.31910153 55.87853411 89.9429229 ] Cluster ID 3
Sample: [71.70723944 32.98917153 70.60028239] Cluster ID 3
Sample: [20.24122881 20.31309653 56.03305737] Cluster ID 5
```

