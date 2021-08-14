import matplotlib.pyplot as plt
import numpy as np

class PCA():
    def __init__(self, matrix):
        self.matrix = self.__shift(matrix)
        
        u, s, vt = np.linalg.svd(self.matrix, full_matrices=False)
        variations = s**2/(len(matrix[0])-1)
        v = np.transpose(vt)
        
        self.singular_values = s
        self.eigenvectors = v[:len(s)]
        self.eigen_values = s**2
        self.PCs = variations/sum(variations)
        
    def __shift(self, matrix):
        new_matrix = []
        for m in matrix:
            av_m = sum(m)/len(m)
            new_row = []
            for i in m:
                new_row.append(i - av_m)

            new_matrix.append(new_row)
        new_matrix = np.transpose(new_matrix)
        return new_matrix

    def __get_project(self, v1, v2):
        v2_norm = np.sqrt(sum(v2**2))
        proj_of_v1_on_v2 = (np.dot(v1, v2)/v2_norm**2)*v2    
        return proj_of_v1_on_v2

    def __get_distance(self, v):
        return np.sqrt(sum(v**2))

    def __get_direction(self, v1, v2):
        bias = np.dot(np.array([1]*len(v2)), v2)
        if np.dot(v1, v2) >= 0:
            return 1*bias
        else:
            return -1*bias
        
    def show_PC_variations(self):
        x = np.arange(len(self.PCs))
        plt.bar(x, (self.PCs * 100).tolist())
        plt.xticks(x, ["PC"+str(i) for i in x])
        plt.xlabel('PCA')
        plt.ylabel('principal components(%)')
        plt.show()

    def show_2_PCA(self, pc1, pc2):
        PC1_proj = [self.__get_project(np.array([i for i in w]), self.eigenvectors[pc1]) for w in self.matrix]
        PC1_direct = [self.__get_direction(np.array([i for i in w]), self.eigenvectors[pc1]) for w in self.matrix]
        PC1_distance =  [d*self.__get_distance(v) for v,d in zip(PC1_proj, PC1_direct)]
        
        PC2_proj = [self.__get_project(np.array([i for i in w]), self.eigenvectors[pc2]) for w in self.matrix]
        PC2_direct = [self.__get_direction(np.array([i for i in w]), self.eigenvectors[pc2]) for w in self.matrix]
        PC2_distance =  [d*self.__get_distance(v) for v,d in zip(PC2_proj, PC2_direct)]
        
        plt.axhline(color='black', lw=0.5)
        plt.axvline(color='black', lw=0.5)
        plt.scatter(PC1_distance, PC2_distance)
        for n in range(len(PC1_distance)):
            plt.annotate(str(n), (PC1_distance[n], PC2_distance[n]))
            
        plt.xlabel("PC" + str(pc1) + " (" + str(round(self.PCs[pc1]*100, 2)) +"%)")
        plt.ylabel("PC" + str(pc2) + " (" + str(round(self.PCs[pc2]*100, 2)) +"%)")
        plt.show()
        
    def show_1_PCA(self, pc1):
        PC1_proj = [self.__get_project(np.array([i for i in w]), self.eigenvectors[pc1]) for w in self.matrix]
        PC1_direct = [self.__get_direction(np.array([i for i in w]), self.eigenvectors[pc1]) for w in self.matrix]
        PC1_distance =  [d*self.__get_distance(v) for v,d in zip(PC1_proj, PC1_direct)]
        
        plt.axhline(color='black', lw=0.5)
        plt.scatter(PC1_distance, [0]*len(PC1_distance))
        for n in range(len(PC1_distance)):
            plt.annotate(str(n), (PC1_distance[n], 0))
        plt.xlabel("PC" + str(pc1) + " (" + str(round(self.PCs[pc1]*100, 2)) +"%)")
        plt.show()