from tkinter.filedialog import askopenfilename

dataset1 = open(askopenfilename(), "r")

if (dataset1.readable()):
    training_dataset = dataset1.read().split("\n")
    print("# of points in training data set: ", len(training_dataset))

    for i in range(len(training_dataset)):
        training_dataset[i]= training_dataset[i].split(",")
        for j in range(len(training_dataset[i])):
            training_dataset[i][j] = float(training_dataset[i][j])

    for v in training_dataset:
        print(v)