import csv
from sklearn import svm
import pickle


point_data = []
x_testing = []

filename = 'raw_model.sav'

def changeDataFormat():
    for item in point_data:
        record = []
        for point in item:
            temp = point.split(', ')
            record.append(temp[0][1:])
            record.append(temp[1][:-1])
        
        x_testing.append(record)

 
def SVMTesting():
    # load the model from disk
    loaded_model = pickle.load(open(filename, 'rb'))
    print(loaded_model)
    
    with open('./dataset/training/CSV/one_v1.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            point_data.append(row)
    
    changeDataFormat()
    print('Total number of data for tested: ' + str(len(point_data)))
    
    counter = 0
    for test_case in x_testing:
        #print(str(test_case) + '\n')
        test = []
        test.append(test_case)
        if(loaded_model.predict(test)[0] == '1'):
            counter += 1
            
    print('Tested % of 1 class: ' + str(counter / len(x_testing)))
    

            
if __name__ == '__main__':
    SVMTesting()