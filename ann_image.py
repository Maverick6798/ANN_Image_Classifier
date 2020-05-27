from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense

(X_train_all,Y_train_all),(X_test_all,Y_test_all)=cifar10.load_data()

Label_names=['plane','Automobile','Bird','Cat','Deer','Dog','Frog','Horse','Ship','Truck']

Image_width=32
Image_height=32
total_pixel=32*32
color_channels=3
Total_inputs=32*32*3


X_train,X_test=X_train_all/255,X_test_all/255
X_train=X_train.reshape(len(X_train),Total_inputs)
X_test=X_test.reshape(len(X_test),Total_inputs)

X_val=X_train[:1000]
Y_val=Y_train_all[:1000]
X_train=X_train[10000:]
Y_train=Y_train_all[10000:]

model=Sequential()
model.add(Dense(units=128,input_dim=Total_inputs,activation='relu'))
model.add(Dense(units=64,activation='relu'))
model.add(Dense(units=16,activation='relu'))
model.add(Dense(units=10,activation='softmax'))

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(X_train,Y_train,batch_size=1000,epochs=100,validation_data=(X_val,Y_val))
print (model.coef_)

from sklearn.externals import joblib
joblib.dump(model,'ann_image_model.pkl')


