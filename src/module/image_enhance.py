import cv2
import os
from config import file_Directory
import numpy as np
class Image_Enhance():

    def __init__(self, image_path) -> None:
        self.image_path = image_path
    
    def brightness_Adjust(self):
        # Load the image 
        image = cv2.imread(self.image_path) 
        #Plot the original image 
        alpha = 1.5  
        # control brightness by 50 
        beta = -150
        image2 = cv2.convertScaleAbs(image, alpha=alpha, beta=beta) 
        #Save the image 
        # imagepth = os.path.join(os.path.dirname(self.image_path), 'Brightness & contrast.jpg')
        imagepth = os.path.join(file_Directory, 'Brightness & contrast.jpg')
        cv2.imwrite(imagepth, image2) 
        return imagepth
    
    def sharpen(self, imagepth):
        image = cv2.imread(imagepth) 
        # Create the sharpening kernel 
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 
        # Sharpen the image 
        sharpened_image = cv2.filter2D(image, -1, kernel) 
        #Save the image
        imagepath = os.path.join(file_Directory, 'sharpened_image.jpg') 
        cv2.imwrite(imagepath, sharpened_image) 
        return imagepath
        

    def lapacian_sharpen(self, imagepth):
        #Load the image 
        image = cv2.imread(imagepth) 
        
        # Sharpen the image using the Laplacian operator 
        sharpened_image2 = cv2.Laplacian(image, cv2.CV_64F) 
        imagepath = os.path.join(file_Directory, 'Laplacian_sharpened_image.jpg') 
        #Save the image 
        cv2.imwrite(imagepath, sharpened_image2) 

    def removing_noise(self, imagepth):
        # Load the image 
        image = cv2.imread(imagepth) 
        # Remove noise using a median filter 
        filtered_image = cv2.medianBlur(image, 1) 
        imagepath = os.path.join(file_Directory, 'Median Blur.jpg') 
        #Save the image 
        cv2.imwrite(imagepath, filtered_image) 

        return imagepath

    
    def enhance_color(self, imagepth):
        # Load the image 
        image = cv2.imread(imagepth) 
        image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV) 
        
        # Adjust the hue, saturation, and value of the image 
        # Adjusts the hue by multiplying it by 0.7 
        image[:, :, 0] = image[:, :, 0] * 0.7
        # Adjusts the saturation by multiplying it by 1.5 
        image[:, :, 1] = image[:, :, 1] * 1.5
        # Adjusts the value by multiplying it by 0.5 
        image[:, :, 2] = image[:, :, 2] * 0.5
        
        image2 = cv2.cvtColor(image, cv2.COLOR_HSV2BGR) 
        imagepath = os.path.join(file_Directory, 'enhanced coloured.jpg') 
        #Save the image 
        cv2.imwrite(imagepath, image2) 
       

obj = Image_Enhance(r"/home/vrush/Catalog-Digitization-/src/module/data/Catalog Digitization/ONDC Test Data _ Images/Product Images/Bru_Instant_Coffee_Powder.png")
pth = obj.brightness_Adjust()
sharpen = obj.sharpen(pth)
lapacian_sharpen = obj.lapacian_sharpen(sharpen)
noise = obj.removing_noise(pth)
obj.enhance_color(noise)