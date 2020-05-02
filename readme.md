# ANN_IMAGE CLASSIFIER

This is an image classifier **Deep Learning model** created with the help of *Artificial Neural Network*

### It detects images using deep learning and python


I will be using **Artificial Neural Network** in this project,in perticular ANN is trained on *CIFAR10* dataset of KERAS.

This Cifar10 datasets consits of 10 labels, including

   1. Plane
   2. Automobile
   3. Cat
   4. Dog 
   5. Deer
   6. Ship
   7. Truck
   8. Frog
   9. Horse
   10. Bird

## Installation

	* pip3 install numpy
	* pip3 install keras
	* pip3 install tensorflow
	* pip3 install flask 
	* Docker

## Working Process

The ANN model is built on python program and later on it is connected to the **flask** which helps it to deploy on webserver.
Webpages are built on HTML.
Docker and Dockerfile is used to convert all of it into an OS(image).
That image is later on pushed on **Docker Hub** for public use.
To pull that image from Docker Hub
		**docker pull maverick6798/ann_image_classifier**
All the files later on are uploaded on github.

## To Run The Project

   1. Download the docker 
   2. Use these command on terminal -
   			***docker pull maverick6798/ann_image_classifier***
  		    ***docker run -dit maverick6798/ann_image_classifier***
   3. Go to your browser and use URL ***0.0.0.0:5000***.
   4. Upload an image of the thing from above list. 

#### NOTE
*There is a chance that docker might not open image. so use command* ***setenforce 0*** *before running the image.*

### NOTE
**This model is built with the accuracy of 51%. So there are 49% chances that the model will not be able to give its correct name.Updates are in process to increase the accuracy of the model.**
