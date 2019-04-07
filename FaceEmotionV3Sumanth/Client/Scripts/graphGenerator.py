from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv

#Converts the merged CSV to Pleasure,Arousal,Dominance
def convertToPADValues:
with open('../CSVDumps/merged.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        numCols = len(row)
        for i in range(0,numCols):
			print(row[i])


if __name__== "__main__":
  mergeDataFromSources()

'''fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x =[1,2,3,4,5,6,7,8,9,10]
y =[5,6,2,3,13,4,1,2,4,8]
z =[2,3,3,3,5,7,9,11,9,10]



ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

#plt.show()
plt.savefig('image.jpg') '''

