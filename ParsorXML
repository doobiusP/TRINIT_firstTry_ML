import xml.etree.ElementTree as ET

# Load XML file
tree = ET.parse('InsertLinktofilelocation') #put your xml file's path here
root = tree.getroot()

# Extract information
folder = root.find('folder').text
filename = root.find('filename').text

size = root.find('size')
width = int(size.find('width').text)
height = int(size.find('height').text)
depth = int(size.find('depth').text)

objects = []
for obj in root.findall('object'):
    name = obj.find('name').text
    pose = obj.find('pose').text
    truncated = int(obj.find('truncated').text)
    difficult = int(obj.find('difficult').text)
    bbox = obj.find('bndbox')
    xmin = int(bbox.find('xmin').text)
    ymin = int(bbox.find('ymin').text)
    xmax = int(bbox.find('xmax').text)
    ymax = int(bbox.find('ymax').text)
    objects.append({
        'name': name,
        'pose': pose,
        'truncated': truncated,
        'difficult': difficult,
        'bbox': {'xmin': xmin, 'ymin': ymin, 'xmax': xmax, 'ymax': ymax}
    })

# Print extracted information
print("Folder:", folder)
print("Filename:", filename)
print("Image Size:", width, "x", height, "x", depth)
print("Objects:")
for obj in objects:
    print("- Name:", obj['name'])
    print("  Pose:", obj['pose'])
    print("  Truncated:", obj['truncated'])
    print("  Difficult:", obj['difficult'])
    print("  Bounding Box:", obj['bbox'])
