# PCA-with-numpy
Introduce Principal Component Analysis(PCA) step by step with numpy
https://hackmd.io/@TKDOgu_kT3yWnqCyIxb3-Q/HyJr68TJt


```
import matplotlib.pyplot as plt
import numpy as np
from PCA import PCA #import PCA module from PCA.py
```

```
#sample 0 ~ 5
f0 = [10, 11, 8, 3, 2, 1]
f1 = [6, 4, 5, 3, 0.7, 1]
f2 = [8, 2, 9, 1.5, 5, 5]
f3 = [7, 6, 5, 4, 8, 8.5]
matrix = np.array([f0,f1,f2,f3])

pca = PCA(matrix)
```

```
pca.eigenvectors

array([[-0.86889937,  0.24093226,  0.33542894, -0.27286069],
       [-0.40900889, -0.02568878, -0.35886838,  0.83860915],
       [-0.25039745, -0.92977389, -0.15847275, -0.21842166],
       [ 0.12258356, -0.27715023,  0.85649711,  0.41782021]])
```

```
pca.eigen_values

array([120.08515057,  44.27951779,  13.30470227,   1.38896271])
```

```
pca.PCs # variance ratio for each PC

array([0.67064821, 0.24729102, 0.07430373, 0.00775704])
```

```
pca.show_PC_variations()
```
![](https://i.imgur.com/xLtWCVm.png)


```
pca.show_2_PCA(0,1)
```
![](https://i.imgur.com/wxQs8zo.png)

```
pca.show_1_PCA(3)
```
![](https://i.imgur.com/qDZPl6c.png)

