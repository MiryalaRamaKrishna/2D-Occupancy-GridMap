import cv2
import numpy as np

def stitch_images(images):
    # Create a stitcher object
    stitcher = cv2.Stitcher_create()
    print (stitcher)
    # Stitch the images
    status, stitched = stitcher.stitch(images)
    print (status)
    if status != cv2.Stitcher_OK:
        print("Error stitching images")
        return None
    return stitched

# Load the images
img1 = cv2.imread('/home/maryann/Downloads/Camera_Image_1.png')
img2 = cv2.imread('/home/maryann/Downloads/Camera_Image_2.png')
img3 = cv2.imread('/home/maryann/Downloads/Camera_Image_3.png')
img4 = cv2.imread('/home/maryann/Downloads/Camera_Image_4.png')
#img1 = cv2.imread('angle1.jpg')
#img2 = cv2.imread('angle2.jpg')
#img3 = cv2.imread('angle3.jpg')
#img4 = cv2.imread('angle4.jpg')

# Check if images are loaded correctly
#if img1 is None or img2 is None or img3 is None or img4 is None:
if img1 is None or img2 is None :
    print("Error loading images")
    exit()

# List of images to be stitched
#images = [img1, img2, img3, img4]
images = [img1, img2]

# Stitch the images
stitched_image = stitch_images(images)
if stitched_image is not None:
    # Save the combined image
    cv2.imwrite('stitched_image.jpg', stitched_image)

    # Display the combined image
    cv2.imshow('Stitched Image', stitched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image stitching failed.")
