from tkinter.filedialog import askopenfilename
from math import *

#this function takes a file and returns a 2D list containing the dataset
def getData(file):
    dataset = file.read().split("\n")
    print("# of points in training data set: ", len(dataset))

    for i in range(len(dataset)):
        dataset[i]= dataset[i].split(",")
        for j in range(len(dataset[i])):
            dataset[i][j] = float(dataset[i][j])

    #for v in dataset:
    #    print(v)
    print(dataset[1])

    return dataset

#select and read the training data set
trainingfile = open(askopenfilename(), "r")
if (trainingfile.readable()):
    training_dataset = getData(trainingfile)
    
    #select and read the input
    inputfile = open(askopenfilename(), "r")
    if (inputfile.readable()):
        unlabelled_points = getData(inputfile)

        #ask user for value of k
        k = int(input("Enter k: "))

        n = len(unlabelled_points[1])     #no. of dimensions
        all_distances = {}

        for i in range(len(unlabelled_points)):
            for j in range(len(training_dataset)):
                #compute for distance
                distance = 0
                for h in range(n):
                    distance = distance + (unlabelled_points[i][h] - training_dataset[j][h])**2
                distance = sqrt(distance)
                all_distances[j] = distance

                if (i==1) and (j==1):
                    print(distance)
            
        sorted_dist = dict(sorted(all_distances.items(), key=lambda item: item[1]))
        nearest_neighbors = list(sorted_dist.keys())[:k]    #contains the index of the k-nearest neighbors

        print(nearest_neighbors)

