# Importe required libraries
import sys
import cv2
from pyzbar.pyzbar import decode
  
# Function to decode barcode from a given image
def barcodeReader(image):
     
    # read the image in numpy array using cv2
    img = cv2.imread(image)
      
    # Decode the barcode image
    detectedBarcodes = decode(img)
      
    # If not detected then print the message
    if not detectedBarcodes:
        print(f"Barcode cannot be decoded from the image {image} or your barcode is blank/ indecipherable!")
    else:
       
          # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes: 
           
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect
             
            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x-10, y-10),
                          (x + w+10, y + h+10),
                          (255, 0, 0), 2)
             
            if barcode.data!="":
               
            # Print the barcode data
                print(barcode.data)
                print(barcode.type)
                 
    # Display the image
    cv2.imshow("Image", img)
    # cv2.waitkey() method waits till we exit or click on the close button
    cv2.waitKey(0)
    # call the sys.exit() method to safely exit the technique
    sys.exit() # to exit from all the processes
    
 
if __name__ == "__main__":
  # Take the image file from user and assign it to a variable image
    image = input("Enter file with bardcode image: ")
    print(f"The file name which you entered is: {image}" )
    barcodeReader(image)

# Destroy all the created windows using cv2.destroyAllWindows()
cv2.destroyAllWindows()