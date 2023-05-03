# Image_processing
- [Q1-Given an image file stored on the computer write a program to read it and
store it in different format (extension) show the effect on the image size on the
disk.]() 
### desription
<<<<<<< HEAD
   - In this program, the file paths for the input and output directories are set in the input_dir and output_dir variables, respectively. The os.path.join function is used to construct the full file paths for the input and output image files.

 - The Image module is used to open the image file from the input directory, and the save method is used to save the image in the output directory with a new filename and extension.

  - The program gets the sizes of the original and converted image files using os.path.getsize and prints the size information to the console. Note that you will need to replace `"/path/to/input/directory"` and `"/path/to/output/directory"` with the actual file paths for your input and output directories.
=======
        1- In this program, the file paths for the input and output directories are set in the input_dir and output_dir variables, respectively. The os.path.join function is used to construct the full file paths for the input and output image files.

        2- The Image module is used to open the image file from the input directory, and the save method is used to save the image in the output directory with a new filename and extension.

        3- The program gets the sizes of the original and converted image files using os.path.getsize and prints the size information to the console. Note that you will need to replace `"/path/to/input/directory"` and `"/path/to/output/directory"` with the actual file paths for your input and output directories.
>>>>>>> 4ab2fe0762ae08cbc7d2815f76e90f6f65d886aa

 - *NOTE*  
        - the file paths in this code use absolute paths, which are specific to the file system on your computer. If you run this code on a different computer, you may need to adjust the file paths to match the file system on that computer.

---

- [Q2. Write a program to read an image and change its type from color image to
gray scale image and to binary image and save the output gray scale and binary
images show the effect on the image size on the disk.]()
### desription

  - In this program, the Image module from PIL is used to open the input image file "example.jpg". The convert method is called on the input_image object to convert it to grayscale ('L') and binary ('1') images, which are stored in the grayscale_image and binary_image objects, respectively. The save method is then called on each of these objects to save the grayscale and binary images to disk as PNG files.

  - The size of the original, grayscale, and binary images are obtained using os.path.getsize, and the size differences between the original and grayscale/binary images are printed to the console. This demonstrates the effect that converting an image to grayscale or binary can have on the file size.

  ---
  