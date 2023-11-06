from tkinter.filedialog import askopenfilename
from math import *

#this function takes a file and returns a 2D list containing the dataset
def getData(file):
    dataset = file.read().split("\n")
    print("# of points in training data set: ", len(dataset))

    for i in range(len(dataset)):
        if (dataset[i] == ''):
            del dataset[i]
        else:
            dataset[i]= dataset[i].split(",")
            for j in range(len(dataset[i])):
                dataset[i][j] = float(dataset[i][j])

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

            classifications = {}
            for neighbor in nearest_neighbors:
                classif = training_dataset[neighbor][n]
                if (classif in classifications.keys()):
                    classifications[classif] = classifications[classif] + 1
                else:
                    classifications[classif] = 1
            
            unlabelled_points[i].append(int(max(classifications, key=classifications.get)))     #append the classification with the highest frequency
            print(unlabelled_points[i])

        #export to output file
        output = open("output.txt", "w")
        for p in unlabelled_points:
            output.write(", ".join(str(e) for e in p) + "\n")
        output.close()