import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import os
import torchvision.transforms as transforms

import xml.etree.ElementTree as ET

# Load the XML file
path_to_imgs = '/Users/vedanthnanesha/Downloads/Japan/train/images/'
all_imgs = os.listdir(path_to_imgs)
all_paths_to_imgs = [path_to_imgs+x for x in all_imgs]

path_to_xmls = '/Users/vedanthnanesha/Downloads/Japan/train/annotations/xmls/' 
all_xmls = os.listdir(path_to_xmls)
all_paths_to_xmls = [path_to_xmls+x for x in all_xmls]

i=0
all_xml_numbers=[]
for x in all_imgs:
    all_xml_numbers.append(x[6:-4])

print(all_xml_numbers)

for number in all_xml_numbers:
    #string = (6-len(str(i)))*"0"+f"{i}"
    img = Image.open(f'/Users/vedanthnanesha/Downloads/Japan/train/images/Japan_{number}.jpg')
    w,h = img.size
    scale_factor = 1
    if w!=600:
        tree = ET.parse(f'/Users/vedanthnanesha/Downloads/Japan/train/annotations/xmls/Japan_{number}.xml') #Comment out this during test manipulation
        root = tree.getroot() #Comment out this during test manipulation
        scale_factor = 600/w
        small_transform = transforms.Resize((600,600))
        img = small_transform(img)
        img.save(f'/Users/vedanthnanesha/Downloads/Japan/train/images/Japan_{number}.jpg')
        # Scale factor

        # Iterate through 'object' elements and update bounding box values
        #Comment out this during test manipulation
        for obj in root.findall('object'):
            bndbox = obj.find('bndbox')
            xmin = int(float(bndbox.find('xmin').text) * scale_factor)
            ymin = int(float(bndbox.find('ymin').text) * scale_factor)
            xmax = int(float(bndbox.find('xmax').text) * scale_factor)
            ymax = int(float(bndbox.find('ymax').text) * scale_factor)

            bndbox.find('xmin').text = str(xmin)
            bndbox.find('ymin').text = str(ymin)
            bndbox.find('xmax').text = str(xmax)
            bndbox.find('ymax').text = str(ymax)

        # Save the modified XML tree back to the file
        #Comment out this during test manipulation
        tree.write(f'/Users/vedanthnanesha/Downloads/Japan/train/annotations/xmls/Japan_{number}.xml')  # Replace with the desired output filename
    
