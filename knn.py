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
        nearest_neighbors = [0]*k   #index of the k-nearest neighbors
        print(nearest_neighbors)

        n = len(unlabelled_points[1])     #no. of dimensions

        for i in range(len(unlabelled_points)):
            for j in range(len(training_dataset)):
                distance = 0
                for h in range(n):
                    distance = distance + (unlabelled_points[i][h] - training_dataset[j][h])**2
                distance = sqrt(distance)
                if (i==1) and (j==1):
                    print(distance)
