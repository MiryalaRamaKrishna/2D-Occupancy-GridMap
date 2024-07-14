import cv2

def stitch_images(images):
    # Check if images list is empty or contains None elements
    if not images or any(img is None for img in images):
        print("Error: Empty or invalid images list.")
        return None
    
    # Create stitcher object based on OpenCV version
    stitcher = cv2.createStitcher() if int(cv2.__version__.split('.')[0]) < 4 else cv2.Stitcher_create()
    
    # Attempt to stitch images
    status, stitched = stitcher.stitch(images)
    
    if status != cv2.Stitcher_OK:
        print("Error stitching images:", status)
        return None
    
    return stitched

def main():
    # Load images from specified paths
    images = []
    for i in range(1, 5):
        img_path = f'/home/maryann/Downloads/Camera_Image_{i}.png'
        img = cv2.imread(img_path)
        
        if img is None:
            print(f"Error: Unable to load image {img_path}")
            return
        
        images.append(img)
    
    # Stitch images
    stitched = stitch_images(images)
    
    if stitched is not None:
        # Save stitched image
        cv2.imwrite('/home/maryann/Downloads/stitched_image.png', stitched)
        print("Stitched image saved successfully.")
    else:
        print("Failed to stitch images.")

if __name__ == '__main__':
    main()

