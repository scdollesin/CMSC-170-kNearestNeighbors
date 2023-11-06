# EXERCISE #7 K NEAREST NEIGHBORS
# AUTHOR: Samantha Shane C. Dollesin
# STUDENT NO.: 2020-01893
# SECTION: WX-1L
# PROGRAM DESCRIPTION: This program takes a two files (the training and input data sets) and a value for k, classifies the unlabelled points in the input
#                      file using the k-nearest neighbors method, and writes the results on an output file and a modified version of the training data set.

from tkinter.filedialog import askopenfilename
from math import *

#this function takes a file and returns a 2D list containing the dataset
def getData(file):
    dataset = file.read().split("\n")

    for i in range(len(dataset)):
        if (dataset[i] == ''):
            del dataset[i]
        else:
            dataset[i]= dataset[i].split(",")
            for j in range(len(dataset[i])):
                dataset[i][j] = float(dataset[i][j])

    print("# of points in data set: ", len(dataset))
    return dataset

#select and read the training data set
trainingfile = open(askopenfilename(), "r")
if (trainingfile.readable()):
    training_dataset = getData(trainingfile)
    trainingfile.close()
    
    #select and read the input
    inputfile = open(askopenfilename(), "r")
    if (inputfile.readable()):
        unlabelled_points = getData(inputfile)
        inputfile.close()

        #ask user for value of k
        k = int(input("Enter k: "))
        n = len(unlabelled_points[1])     #no. of dimensions

        for i in range(len(unlabelled_points)):
            all_distances = {}

            for j in range(len(training_dataset)):
                #compute for distance
                distance = 0
                for h in range(n):
                    distance = distance + (unlabelled_points[i][h] - training_dataset[j][h])**2     #summation
                distance = sqrt(distance)
                all_distances[j] = distance
            
            sorted_dist = dict(sorted(all_distances.items(), key=lambda item: item[1]))
            nearest_neighbors = list(sorted_dist.keys())[:k]    #contains the index of the k-nearest neighbors

            #for n in nearest_neighbors:
            #    print(sorted_dist[n])    #print distances of the nearest neighbors

            #count the frequency of each classification
            classifications = {}
            for neighbor in nearest_neighbors:
                classif = training_dataset[neighbor][n]
                if (classif in classifications.keys()):
                    classifications[classif] = classifications[classif] + 1
                else:
                    classifications[classif] = 1
            
            unlabelled_points[i].append(int(max(classifications, key=classifications.get)))     #append the classification with the highest frequency
            print(unlabelled_points[i])

            training_dataset.append(unlabelled_points[i])      #add the newly labelled point to the training data

        #export the modified training data set to a new csv file
        csv = open("modified training data.csv", "w")
        for p in training_dataset:
            csv.write(", ".join(str(e) for e in p) + "\n")
        csv.close()

        #export newly labelled points to its own output file
        output = open("output.txt", "w")
        for p in unlabelled_points:
            output.write(", ".join(str(e) for e in p) + "\n")
        output.close()
        