# TRINIT_firstTry_ML
Repository for ML Track Problem Statement 1 of Tri-NIT Hackathon 2024 by the team 'firstTry'

Members:
- Aaryan Patil
- Vedanth Nanesha
- Alen Basil
- Tanay Shekokar

## Structure of the Repository:
The repository contains an XML parser and 2 .ipynb files that have been used to data-augment the existing dataset to ensure all images are 600x600 in size whilst also adjusting their corresponding bounding box coordinates. **Augmented files are already provided** for in the following kaggle link to the merged dataset. 

**The model** is presented as 2 .ipynb files, 1 being the file used for training and visualising progress of the Faster R-CNN during training and the other being a file containing the minimal dependencies required to use the model for testing. Both .ipynb files contain markdown for easier navigation.

## Using the Repository:
To *test* the model, be it locally or on a site such as kaggle, provide the relative path inside your dataset to a folder that contains all testing images that should be classified. The testing code will display the first 20 images alongside their generated bounding boxes and associated labels. (WE NEED TO MAKE IT SO THAT THEIR ANNOTATIONS FOLDER CAN ALSO BE USED)

To *train* the model using kaggle, connect to our publicly available dataset (link here) to a notebook and press 'Run All' to begin training. Statistics for every set of iterations will be printed in the log for tracking.


