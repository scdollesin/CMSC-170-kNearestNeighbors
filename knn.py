from tkinter.filedialog import askopenfilename

def getData(file):
    dataset = file.read().split("\n")
    print("# of points in training data set: ", len(dataset))

    for i in range(len(dataset)):
        dataset[i]= dataset[i].split(",")
        for j in range(len(dataset[i])):
            dataset[i][j] = float(dataset[i][j])

    for v in dataset:
        print(v)
    
    return dataset

#select and read the training data set
trainingfile = open(askopenfilename(), "r")
if (trainingfile.readable()):
    training_dataset = getData(trainingfile)
    
    #select and read the input
    inputfile = open(askopenfilename(), "r")
    if (inputfile.readable()):
        unlabelled_points = getData(inputfile)