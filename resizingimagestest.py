import os 
from PIL import Image 

path_to_imgs = '/Users/vedanthnanesha/Desktop/temp/'
all_imgs = os.listdir(path_to_imgs)
all_paths_to_imgs = [os.path.join(path_to_imgs, x) for x in all_imgs]

for img_path in all_paths_to_imgs:
    if os.path.isfile(img_path):
        try:
            img = Image.open(img_path)
            w, h = img.size
            if w != 600:
                img = img.resize((600, 600))
                img.save(img_path)
            img.close()
        except (IOError, OSError):
            print(f"Skipping {img_path} as it's not a valid image file.")

print("Images resized.")
