# Faster R-CNN Implementation by firstTry
Repository for ML Track Problem Statement 1 of Tri-NIT Hackathon 2024 by the team 'firstTry'

Members:
- Aaryan Patil
- Vedanth Nanesha
- Alen Basil
- Tanay Shekokar

## Structure of the Repository:
The repository contains an XML parser and 2 python files that have been used to data-augment the existing dataset to ensure all images are 600x600 in size whilst also adjusting their corresponding bounding box coordinates. **Augmented files are already provided** for in the following <a href="https://www.kaggle.com/datasets/vedanthnanesha/road-images-dataset-for-road-fault-detection/data">kaggle link</a> to the merged dataset. 

**The model** is presented as 2 .ipynb files, 1 being the file used for training and visualising progress of the Faster R-CNN during training and the other being a file containing the minimal dependencies required to use the model for testing. Both .ipynb files contain markdown for easier navigation.

Pretrained parameters are uploaded as *'FasterRCNN_Params.pth'* which can be loaded into the testing .ipynb file.

## Using the Repository:
To *test* the model, be it locally or on a site such as kaggle, provide the relative path inside your dataset to a folder that contains all testing images that should be classified. The testing code will display the first 20 images alongside their generated bounding boxes and associated labels.

To *train* the model using kaggle, connect to our publicly available dataset (link above) to any notebook and press 'Run All' to begin training. Statistics for every set of iterations will be printed in the log for tracking.

Alternatively, the original *rough* code for training Faster R-CNN exists in this public <a href="https://www.kaggle.com/code/vedanthnanesha/faster-rcnn-for-road-faults/notebook" target="_blank"> kaggle notebook </a>. Accordingly, the original *rough* code for testing the Faster R-CNN exists in this public <a href="https://www.kaggle.com/code/alenbasil/faster-rcnn-for-testing/notebook"> kaggle notebook </a>. 

## Sample test images:
![Sample Output Image](https://github.com/doobiusP/TRINIT_firstTry_ML/blob/main/sample_output0.jpeg?raw=True)
![Sample Output Image](https://github.com/doobiusP/TRINIT_firstTry_ML/blob/main/sample_output1.jpeg?raw=True)
![Sample Output Image](https://github.com/doobiusP/TRINIT_firstTry_ML/blob/main/sample_output2.jpeg?raw=True)

