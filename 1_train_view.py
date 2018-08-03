from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import *

train_directory = r'F:\xampp\htdocs\training_cow\fview'          
check_directory = r'F:\xampp\htdocs\validation_cow\fview'       	

no_of_training_samples = 4 	
no_of_validation_samples = 2	
epoch = 10
batch_size = 1


height, width = 150, 150


model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape = (width, height, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.4))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics = ['accuracy'])



inp_data = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2)
input_data = inp_data.flow_from_directory(train_directory, target_size=(150, 150), batch_size = 1, class_mode = 'categorical')
