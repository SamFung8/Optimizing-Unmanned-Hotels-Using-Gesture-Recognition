import csv
from sklearn import svm
import pickle


data = ['1','2','3','4','5','6','7','8','9']
point_data = []
x_training = []
y_training = []

clf = svm.SVC()
filename = 'raw_model.sav'

def loadCSVFile():
    for item in data:
        with open('./dataset/training/CSV/raw_' + str(item) + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                point_data.append(row)
                y_training.append(item)
                
    changeDataFormat()            


def changeDataFormat():
    for item in point_data:
        record = []
        for point in item:
            temp = point.split(', ')
            record.append(temp[0][1:])
            record.append(temp[1][:-1])
        
        x_training.append(record)


def SVMModel():
    print('Total number of data for training: ' + str(len(x_training)))
    
    clf.fit(x_training, y_training)

    # save the model to disk
    pickle.dump(clf, open('./model/SVM/' + filename, 'wb'))
    
            
if __name__ == '__main__':
    loadCSVFile()
    SVMModel()
    
    print('Training finished and saved the mode as: ' + './model/SVM/' + filename)
    