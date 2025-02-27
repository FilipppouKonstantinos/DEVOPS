# A simple NN using tensorflow

# Libraries

from p_kaggle import p_kaggle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense 

 
def simple_NN(nodes_first_layer,epochs,searchname):
    
    title = ""
    creator = ""
    # load the dataset
    # dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
    
    # Call the kaggle function
    
    X,y,input_shape = p_kaggle(searchname)
        
    # number of nodes of first layer
    
    nodes_first_layer = nodes_first_layer
    
    # split into input (X) and output (y) variables
    #X = dataset[:,0:8]
    #y = dataset[:,8]
    
    # define the keras model
    model = Sequential()
    model.add(Dense(nodes_first_layer, input_shape=(input_shape,), activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    
    # compile the keras model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    # fit the keras model on the dataset
    model.fit(X, y, epochs=epochs, batch_size=10)
    
    # evaluate the keras model
    # The evaluate() function will return a list with two values. 
    # The first will be the loss of the model on the dataset, and the second will be the accuracy of the model on the dataset
    loss, accuracy = model.evaluate(X, y)
    print('Accuracy: %.2f' % (accuracy*100))
    
    return (loss,accuracy)
    
    




