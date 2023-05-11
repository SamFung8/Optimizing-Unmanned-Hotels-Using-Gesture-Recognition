import csv
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

data = ['0','1','2','3','4','5','6','7','8','9']
point_data = []
x_data = []
y_data = []
filename = 'gesture_model.keras'


trainingSetData = 10 * [0]
valSetData = 10 * [0]



def combineAllCSV():
    os.remove('./dataset/training/CSV/All_Training_Data.csv')
    with open('./dataset/training/CSV/All_Training_Data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        temp = x_data
        for i in range(0, len(y_data)):
            writer.writerow(np.append(temp[i], y_data[i]))


def loadCSVFile():
    for item in data:
        with open('./dataset/training/CSV/' + str(item) + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                point_data.append(row)
                y_data.append(item)
    changeDataFormat()


def changeDataFormat():
    global x_data, y_data
    for item in point_data:
        record = []
        for point in item:
            temp = point.split(', ')
            record.append(float(temp[0][1:]))
            record.append(float(temp[1][:-1]))
        x_data.append(record)

    x_data = np.array(x_data)
    y_data = np.array(y_data)


def DNNNetwork():
    network = Sequential()
    network.add(Dense(42, input_shape=(x_data.shape[1],), activation='relu'))
    network.add(Dropout(0.20))
    network.add(Dense(30, activation='relu'))
    network.add(Dropout(0.20))
    network.add(Dense(20, activation='relu'))
    network.add(Dropout(0.20))
    network.add(Dense(10, activation='softmax'))
    network.summary()
    return network


def dataSummaryInfo(y_train, y_val):
    print('\n\n')
    print('Total number of data for training: ' + str(len(x_data)))
    print('Training data and validation data summary:\n')
    for i in y_train:
        trainingSetData[int(i)] += 1
    for i in y_val:
        valSetData[int(i)] += 1
    for item in data:
        print('Training Set of class ' + str(item) + ' has ' + str(trainingSetData[int(item)]) + ' samples ')
        print('Validation Set of class ' + str(item) + ' has ' + str(valSetData[int(item)]) + ' samples ')
    print('\n\n')


def training():
    x_train, x_val, y_train, y_val = train_test_split(x_data, y_data, test_size=0.2, stratify=y_data)
    dataSummaryInfo(y_train, y_val)

    model = DNNNetwork()
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    history = model.fit(x_train, y_train, epochs=800, batch_size=100, validation_data=(x_val, y_val))

    modelVisualization(history)
    modelEvaluation(model)


def modelVisualization(history):
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.savefig('./model/DNN/Model_Accuracy.png')
    plt.show()

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.savefig('./model/DNN/Model_Loss.png')
    plt.show()


def modelEvaluation(model):
    _, accuracy = model.evaluate(x_data, y_data)
    print('The model accuracy: %.2f' % (accuracy * 100))
    model.save('./model/DNN/' + filename)



if __name__ == '__main__':
    loadCSVFile()
    combineAllCSV()

    training()

    print('Training finished and saved the model at: ' + './model/DNN/' + filename)
