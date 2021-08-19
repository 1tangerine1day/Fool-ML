import numpy as np
import matplotlib.pyplot as plt

class DBSCAN():
    def __init__(self, data, radius=5, minPts=5):
        self.radius = radius
        self.minPts = minPts
        self.data = data
        self.cluster_nums, self.cluster_count = self.__do_dbscan(np.transpose(self.data))
 
        
    def __do_dbscan(self, data):
        clusterId = 1
        nPoints = len(data)
        clusterRes = [-1] * nPoints
        for pointId in range(nPoints):
            if clusterRes[pointId] == -1:
                if self.__to_cluster(data, clusterRes, pointId, clusterId):
                    clusterId = clusterId + 1
                    
        return np.asarray(clusterRes), clusterId
    
    def __dist(self, a, b):
        return np.sqrt((np.power(a-b, 2).sum()))

    def __neighbor_points(self, data, pointId):
        points = []
        for i in range(len(data)):
            if self.__dist(data[i], data[pointId]) < self.radius:
                points.append(i)
        return np.asarray(points)

    def __to_cluster(self, data, clusterRes, pointId, clusterId):
        
        points = self.__neighbor_points(data, pointId)
        points = points.tolist()

        queue = []

        if len(points) < self.minPts:
            clusterRes[pointId] = 0
            return False
        else:
            clusterRes[pointId] = clusterId
        for point in points:
            if clusterRes[point] == -1:
                queue.append(point)
                clusterRes[point] = clusterId

        while queue != []:
            neighborRes = self.__neighbor_points(data, queue.pop(0))
            #core
            if len(neighborRes) >= self.minPts:        
                for i in range(len(neighborRes)):
                    resultPoint = neighborRes[i]
                    if clusterRes[resultPoint] == -1:
                        queue.append(resultPoint)
                        clusterRes[resultPoint] = clusterId
                    elif clusterRes[clusterId] == 0:
                        clusterRes[resultPoint] = clusterId
        return True
    
    def show_graph(self):
        if len(self.data) == 2:
            plt.scatter(self.data[0], self.data[1])
            for i, txt in enumerate(self.cluster_nums):
                plt.annotate(txt, (self.data[0][i], self.data[1][i]))
            plt.show()
        else:
            print("only support for two dim")
            
    def show(self):
        c = self.cluster_nums
        for i,j in zip(self.data.T, c) :
            print("Sample:", i, "Cluster ID:", j)