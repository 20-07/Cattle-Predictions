from __future__ import print_function
import keras,os,pandas
import numpy as np
from PIL import Image
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras import metrics
from keras.optimizers import adam
import h5py

data = {}
a = 0
batch_size=30
num_classes=0
epochs=100
x_train=[]
y_train=[]
x_test=[]
y_test=[]
width,height=260,150
training_samples = 0      #60*5  11 eval

for filename in os.listdir('F:\\xampp\\htdocs\\training_cow\\muzzle'):
    idx = filename.find('_')
    st = filename[0:idx]
    if st not in data:
        a = a + 1
        data[st] = a



for filename in os.listdir('F:\\xampp\\htdocs\\training_cow\\muzzle'):
    idx = filename.find('_')
    st = filename[0:idx]
    img = Image.open(os.path.join('F:\\xampp\\htdocs\\training_cow\\muzzle',filename))  
    x_train.append(np.array(img))
    y_train.append(data[st])
    training_samples = training_samples + 1
        

for filename in os.listdir('F:\\xampp\\htdocs\\training_cow\\muzzle_additional'):
    idx = filename.find('_')
    st = filename[0:idx]
    img = Image.open(os.path.join('F:\\xampp\\htdocs\\training_cow\\muzzle_additional',filename))
    x_train.append(np.array(img))
    y_train.append(data[st])
    training_samples = training_samples + 1

for filename in os.listdir('F:\\xampp\\htdocs\\validation_predict_cow\\muzzle'):
    img = Image.open(os.path.join('F:\\xampp\\htdocs\\validation_predict_cow\\muzzle',filename))
    x_test.append(np.array(img))


y_test = [1,1,1,1,  2,2,2,2     ]
print ((x_train).shape)
num_classes = a+1
x_train=np.array(x_train)
y_train=np.array(y_train)
y_test=np.array(y_test)
x_test=np.array(x_test)
#print (type(x_train))
print ((x_train).shape)
x_train = x_train.reshape(x_train.shape[0],3,height,width)
x_test = x_test.reshape(x_test.shape[0],3,height,width)



input_shape = (3,height,width)

y_train=keras.utils.to_categorical(y_train,num_classes)
y_test=keras.utils.to_categorical(y_test,num_classes)
#print(y_train,'train samples')


model=Sequential()
model.add(Conv2D(32,kernel_size=(3, 3),activation='relu', input_shape=input_shape, data_format='channels_first'))
model.add(Conv2D(64,(3, 3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))


model.add(Flatten())
model.add(Dense(1024,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes,activation='softmax'))

print (len(model.layers))
model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.adam(lr=0.000001), metrics=['accuracy'])

model.fit(x_train,y_train,batch_size=batch_size,epochs=epochs,verbose=1,validation_data=(x_test, y_test))
score = model.evaluate(x_test,y_test,verbose=1)
model.save("muzzlemodelnew2.h5")
#print (model.summary())
print('Test loss:', score[0])
print('Test accuracy:', score[1])
