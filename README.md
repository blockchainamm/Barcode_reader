# Barcode reader script

This python script can read barcode(s) from a given image.

The pyzbar library in python is used to decode the rectangles in the barcode.

The pyzbar can return 3 fields based on the barcode object:

- Type: There are several kinds of barcodes available. Which are differentiated by unique code names like CODE-128, Code-11, CODE-39 etc. 
- Data: This is data that is embedded inside the barcode. This data is of various kinds ( alphanumerical, numerical, binary, etc..) depending on the type of barcode.
- Location: This is the collection of points that are located in the code. For barcodes, these points are starting and ending line boundaries.

For a given image such as,

![image](https://github.com/blockchainamm/blockchainamm/assets/82846751/8009d9df-beb1-4e4d-b772-28952a6691c9) 

The script decodes and adds a rectangle framing the barcode as shown below,

![barcode_decoded](https://github.com/blockchainamm/blockchainamm/assets/82846751/9ec2d9db-377b-416f-8211-edcdf17f8b45)
