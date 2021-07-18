# Face Mask Detector
   The ongoing novel coronavirus pandemic situation is known to each and every individual. 
Almost every country has been affected by the devastating Coronavirus(COVID-19) disease. 
The pandemic threatens to reverse hard-won gains made in global health and human capital over the past decade. 
The mandated confinement and social distancing measures in force during an extended period of time, 
will make it beneficial to flatten the curve of transmission.
Artificial intelligence could play an important part in the post-COVID recovery, 
helping to boost productivity and foster a new generation of innovative companies. 
While this situation happens to worsen day by day, it is very much essential for everyone to follow some rules in order to remain safe than to get badly affected with its consequences.
   Here, I have tried to design a custom deep learning model of Face Mask Detector using OpenCV,
Keras/Tensorflow libraries which detects if an individual is wearing a face mask or not and alerting for the same.

# Implementation
   The Face Mask Detection, here, is applied in two different stages. First stage constituting training of Face Mask Detector 
and second stage dealing with applying Face Mask Detector model on to the test images or realtime video streaming. 
   For the first stage, we start with loading the face mask dataset initially, following it with the training of face mask classifier using some of Keras and Tensorflow libraries and lastly serializing face mask classifier to disk.
   In second stage, firstly we load the face mask classifier from disk. The we use it to detect faces in image or video stream and extract the region of interest for each face.
We then apply face mask classifier to each region of interest part of the face to determine whether person has wore mask or not and at last display the results.
We also find the accuracy earned in determining the correct result.
   
