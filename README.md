Module1:Beautify




SRH UNIVERSITY OF APPLIED SCIENCES
Professor: Mr.Alexander Iliev

*************************************************************************** OpenCV,Python 3.2,Pandas,NumPy,PIL*******************************************************************************************************************


Introduction:

PIL:		It is an open-source image handling library written in Python.programming language that adds support for opening, manipulating, and saving many different image file formats.
Pandas:		It is a Python package providing fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data. 
			It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python.
			In addition to this it has the broader goal of becoming the most powerful and flexible open source data analysis/manipulation tool available in any language.    
NumPy:		It is the fundamental package needed for scientific computing in Python.It provides sophisticated (broadcasting) functions,tools for integrating C/C++ and 
			Fortran code,useful linear algebra, Fourier transform, and random number capabilities.
openCV:		It is an open source computer vision and machine learning software library. It has more than 2500 optimized algorithms, which can be used to detect and recognize faces, 
			identify objects, classify human actions in videos, track camera movements, track moving objects, extract 3D models of objects, 
			produce 3D point clouds from stereo cameras, stitch images together to produce a high resolution image of an entire scene etc. 
Colab:		Google Colab is a free cloud service which supports free GPU! You can: improve your Python programming language coding skills.
Harcascade:	It is a classifier which is used to detect the object for which it has been trained for, from the source.The Haar Cascade is trained by superimposing 
			the positive image over a set of negative images. The training is generally done on a server and on various stages. 
			In this project we have used haarcascade_frontalface_default.xml

Course Description:		Emotion recognition using video with the help of Keras(tensorflow as backend engine), Open cv, Pandas, Numpy.
						This course include the presentation ,media files, module.py files, Trained model, weights and readme.txt files.


Prerequisites:
1.) Create project on google colab
2.) Installing Python 3.0
3.) Installing numpy.
4.)Install PIL 1.7
5.)Install openCV
* Windows
* Mac OS
* Linux

****************************************************************************Dependencies********************************************************************************************************************

*pip install numpy
*pip install scikit-image
*pip install pillow
*pip install face_recognition
*pip install opencv-python


****************************************************************************Files to include***************************************************************************************************************
Harcascade = ./haarcascade_frontalface_default.xml. ./haarcascade_eyes.xml



**************************************************************************** module files****************************************************************************************************************
makeup.py:-  Reading dataset using pandas,Designing CNN network training the model and storing model in .json file and weights in .h5 file.
Module_1.py:- capture the video using opencv,Detecting the face using haarcascade_frontalface_default.xml and predicting the emotion using model.

***********************Acknowledgements*********************************************************
https://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html
http://students.iitk.ac.in/eclub/assets/tutorials/OPENCV%20TUTORIAL.pdf
https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/
https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
https://www.tutorialspoint.com/opencv/opencv_scharr_operator.htm
https://www.learnopencv.com/filling-holes-in-an-image-using-opencv-python-c/
https://www.learnopencv.com/opencv-threshold-python-cpp/
https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html?highlight=floodfill
https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html?highlight=dilate#void%20dilate(InputArray%20src,%20OutputArray%20dst,%20InputArray%20kernel,%20Point%20anchor,%20int%20iterations,%20int%20borderType,%20const%20Scalar&%20borderValue)
https://docs.opencv.org/trunk/d0/d86/tutorial_py_image_arithmetics.html
https://www.datacamp.com/community/tutorials/face-detection-python-opencv
https://medium.com/@me.satyam/haar-cascade-face-identification-aa4b8bc79478
https://docs.opencv.org/master/d0/d86/tutorial_py_image_arithmetics.html
**************************************************************************************THE END******************************************************************************************************

