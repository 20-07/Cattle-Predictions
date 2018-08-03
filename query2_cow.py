#!F:\Other_Py\python   

import keras,os
import numpy as np
from PIL import Image
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import urllib.parse as urlparse
from keras.models import load_model
import h5py

############

print ("Content-Type: text/html")
print ("")
import cgi,cgitb

##########
a=0
data= {}

for filename in os.listdir('F:\\xampp\\htdocs\\training_cow\\muzzle'):
    idx1 = filename.find('_')
    idx2 = filename.find(')')
    st = filename[idx1+1:idx2+1]
    if st not in data:
        a = a + 1
        data[st] = a

formobject=cgi.FieldStorage()
img_id = formobject.getvalue('id')

x_predict = []
width,height=260, 150
model = keras.models.load_model("cow_query2_muzzlemodel.h5")

for filename in os.listdir('F:\\xampp\\htdocs\\validation_predict_cow\\muzzle'):
    idx = filename.find('.')
    st = filename[0:idx]
    if img_id==st:
        img = Image.open(os.path.join('F:\\xampp\\htdocs\\validation_predict_cow\\muzzle\\'+filename))
        img = img.resize((width,height), Image.ANTIALIAS)
        x_predict.append(np.array(img))
    

x_predict=np.array(x_predict)
x_predict = x_predict.reshape(x_predict.shape[0],3,height,width)

#print (x_predict.shape)
prediction = model.predict(x_predict,verbose=0)
max = -1
for i in prediction[0]:
    if i > max:
        max = i
for i in range(0,prediction[0].size):
    if prediction[0][i]==max:
        break
for x in data:
    if data[x]==i:
        break
print ("Muzzle View Model: ",x)





x_predict = []
width,height=100, 210
model = keras.models.load_model("cow_query2_fviewmodel.h5")

for filename in os.listdir('F:\\xampp\\htdocs\\validation_predict_cow\\fview'):
    idx = filename.find('.')
    st = filename[0:idx]
    if img_id==st:
        img = Image.open(os.path.join('F:\\xampp\\htdocs\\validation_predict_cow\\fview\\'+filename))
        img = img.resize((width,height), Image.ANTIALIAS)
        x_predict.append(np.array(img))
    

x_predict=np.array(x_predict)
x_predict = x_predict.reshape(x_predict.shape[0],3,height,width)

#print (x_predict.shape)
prediction = model.predict(x_predict,verbose=0)
max = -1
for i in prediction[0]:
    if i > max:
        max = i
for i in range(0,prediction[0].size):
    if prediction[0][i]==max:
        break
for x in data:
    if data[x]==i:
        break
print('<br>')
print('<br>')
print ("Front View Model: ",x)

print('<br>')
print('<br>')
print ("Side View Model: Not Trained")









    
 
