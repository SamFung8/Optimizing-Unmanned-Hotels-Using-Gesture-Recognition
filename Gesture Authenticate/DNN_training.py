import csv
import os

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import numpy as np
import matplotlib.pyplot as plt

data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#data = ['1', '2', '3', '4']
point_data = []
x_training = []
y_training = []


filename = 'raw_model.keras'


def loadCSVFile():
    for item in data:
        with open('./dataset/training/CSV/raw_' + str(item) + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                point_data.append(row)
                y_training.append(item)

    changeDataFormat()


def changeDataFormat():
    global x_training, y_training
    for item in point_data:
        record = []
        for point in item:
            temp = point.split(', ')
            record.append(float(temp[0][1:]))
            record.append(float(temp[1][:-1]))

        x_training.append(record)
    x_training = np.array(x_training)
    y_training = np.array(y_training)


def SVMModel():
    print('Total number of data for training: ' + str(len(x_training)))
    print(type(x_training[0][0]))

    # define the keras model
    model = Sequential()
    model.add(Dense(42, input_shape=(x_training.shape[1],), activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(22, activation='softmax'))
    model.summary()

    # compile the keras model
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # fit the keras model on the dataset
    history = model.fit(x_training, y_training, epochs=500, batch_size=50, validation_split=0.1)

    # 绘制训练 & 验证的准确率值
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()

    # 绘制训练 & 验证的损失值
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()


    # evaluate the keras model
    _, accuracy = model.evaluate(x_training, y_training)
    print('Accuracy: %.2f' % (accuracy * 100))
    model.save('./model/DNN/' + filename)


def saveALL():
    os.remove('./dataset/training/CSV/allData.csv')
    with open('./dataset/training/CSV/allData.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        print(len(x_training))
        temp = x_training
        for i in range(0, len(y_training)):
            writer.writerow(np.append(temp[i], y_training[i]))

if __name__ == '__main__':
    loadCSVFile()
    saveALL()
    SVMModel()

    print('Training finished and saved the mode as: ' + './model/DNN/' + filename)
