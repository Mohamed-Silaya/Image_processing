# Image_processing
- [Q1-Given an image file stored on the computer write a program to read it and
store it in different format (extension) show the effect on the image size on the
disk.]() 
### desription
        1- In this program, the file paths for the input and output directories are set in the input_dir and output_dir variables, respectively. The os.path.join function is used to construct the full file paths for the input and output image files.

        2- The Image module is used to open the image file from the input directory, and the save method is used to save the image in the output directory with a new filename and extension.

        3- The program gets the sizes of the original and converted image files using os.path.getsize and prints the size information to the console. Note that you will need to replace `"/path/to/input/directory"` and `"/path/to/output/directory"` with the actual file paths for your input and output directories.

 - *NOTE*  
        - the file paths in this code use absolute paths, which are specific to the file system on your computer. If you run this code on a different computer, you may need to adjust the file paths to match the file system on that computer.

---
