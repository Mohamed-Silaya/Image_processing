<div align="center">
  <img src="https://techsparks.co.in/wp-content/uploads/2020/12/image-processing.jpg" width="450"/>
</div>



<div id="badges" align="center">
  <a href="[https://www.linkedin.com/in/mohamed-samir-8b585b14a/](https://github.com/opencv/opencv)">
    <img src="https://img.shields.io/badge/OpenCv-Profile-informational?style=flat&logo=OpenCv&logoColor=white&color=0D76A8" alt="OpenCv Badge"/>
  </a>
   <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-Profile-informational?style=flat&logo=Python&logoColor=white&color=0D76A8" alt="python Badge"/>
  </a>
   <a href="https://numpy.org/">
    <img src="https://img.shields.io/badge/Numpy-Profile-informational?style=flat&logo=Numpy&logoColor=white&color=0D76A8" alt="Numpy Badge"/>
  </a>
   <a href="https://matplotlib.org/">
    <img src="https://img.shields.io/badge/MatPlotlib-Profile-informational?style=flat&logo=Matplotlib&logoColor=white&color=0D76A8" alt="matPlotlib Badge"/>
  </a>   
   </div>
   
<div align="center">
   <h1> :eye_speech_bubble:	Image_processing :</h1>
</div>




- [Q1-Given an image file stored on the computer write a program to read it and
store it in different format (extension) show the effect on the image size on the
disk.](https://github.com/Mohamed-Silaya/Image_processing/blob/main/q1.py) 
### desription
   - In this program, the file paths for the input and output directories are set in the input_dir and output_dir variables, respectively. The os.path.join function is used to construct the full file paths for the input and output image files.

 - The Image module is used to open the image file from the input directory, and the save method is used to save the image in the output directory with a new filename and extension.

  - The program gets the sizes of the original and converted image files using os.path.getsize and prints the size information to the console. Note that you will need to replace `"/path/to/input/directory"` and `"/path/to/output/directory"` with the actual file paths for your input and output directories.
=======
        1- In this program, the file paths for the input and output directories are set in the input_dir and output_dir variables, respectively. The os.path.join function is used to construct the full file paths for the input and output image files.

        2- The Image module is used to open the image file from the input directory, and the save method is used to save the image in the output directory with a new filename and extension.

        3- The program gets the sizes of the original and converted image files using os.path.getsize and prints the size information to the console. Note that you will need to replace `"/path/to/input/directory"` and `"/path/to/output/directory"` with the actual file paths for your input and output directories.

 - *NOTE*  
        - the file paths in this code use absolute paths, which are specific to the file system on your computer. If you run this code on a different computer, you may need to adjust the file paths to match the file system on that computer.

---

- [Q2. Write a program to read an image and change its type from color image to
gray scale image and to binary image and save the output gray scale and binary
images show the effect on the image size on the disk.](https://github.com/Mohamed-Silaya/Image_processing/blob/main/q2.py)
### desription

  - In this program, the Image module from PIL is used to open the input image file "example.jpg". The convert method is called on the input_image object to convert it to grayscale ('L') and binary ('1') images, which are stored in the grayscale_image and binary_image objects, respectively. The save method is then called on each of these objects to save the grayscale and binary images to disk as PNG files.

  - The size of the original, grayscale, and binary images are obtained using os.path.getsize, and the size differences between the original and grayscale/binary images are printed to the console. This demonstrates the effect that converting an image to grayscale or binary can have on the file size.

  ---

- [Q3. Write a program to read an image resize it to be half the width and height.
The program should read the file and print the width, height and resolution
before and after resize.](https://github.com/Mohamed-Silaya/Image_processing/blob/main/q3.py)

### description

 - In this program, the `Image` module from PIL is used to open the input image file "example.jpg". The `size` attribute of the `input_image` object is used to obtain the width and height of the original image, and the `info` attribute is used to obtain the resolution of the image.

 -  The original image information is printed to the console, and the `resize` method is called on the `input_image` object to resize the image to half the width and height. The resulting `resized_image` object is used to obtain the resized image width, height, and resolution, which are printed to the console.

 -  The `save` method is called on the `resized_image` object to save the resized image to disk as a JPEG file named "New-Pic_resized.jpg".

 ---
 - [Q4. Write a program to read a color image and split it into R, G, B channels.
Display each of them and store them as gray scale image to the computer.](https://github.com/Mohamed-Silaya/Image_processing/blob/main/q4.py)

### description
 -  In this program, the Image module from PIL is used to open the input image file "Old-Pic.png". The split method is called on the input_image object to split the image into its R, G, and B channels, which are stored in the r_channel, g_channel, and b_channel objects, respectively.

 -  The show method is then called on each of these objects to display the R, G, and B channels. Note that this will open a new window for each channel showing the grayscale version of the channel.

 -  The convert method is called on each of the R, G, and B channels to convert them to grayscale, and the save method is called on each of the grayscale channels to save them to disk as PNG files named "New_r_grayscale.png", "New_g_grayscale.png", and "New_b_grayscale.png", respectively.

 *NOTE*
 > What is 'L' in r_grayscale = r_channel.convert('L') ?

  - The 'L' mode in Pillow is a grayscale mode that uses a single channel to represent the brightness or intensity of each pixel in the image. In contrast, other grayscale modes like 'LA', 'RGBX', and 'RGBA' use multiple channels to represent grayscale values.

  - The 'LA' mode is a grayscale mode that uses two channels to represent grayscale values and alpha (transpa rency) values. The first channel represents the grayscale value, and the second channel represents the alpha value.

 -  The 'RGBX' mode is a grayscale mode that uses three channels to represent grayscale values. Each channel represents a different color (red, green, or blue) and is used to calculate the grayscale value of each pixel.

  - The 'RGBA' mode is a grayscale mode that uses four channels to represent grayscale values and alpha values. The first three channels represent the red, green, and blue values, and the fourth channel represents the alpha value.

  - In general, the choice of grayscale mode depends on the specific needs of the application and the image being processed. The 'L' mode is a good choice for most grayscale applications because it is simple and efficient, using only one channel to represent grayscale values. However, in some cases, other grayscale modes like 'LA', 'RGBX', and 'RGBA' may be more appropriate, depending on the specific requirements of the application.

---
 - [Q5. Write a program to read an image convert to gray scale then calculate and
show its histogram. (Apply this program twice first using open cv function for
histogram and second without using the function)](https://github.com/Mohamed-Silaya/Image_processing/blob/main/q5.py)

### description

 -  In this program, the cv2 module from OpenCV is used to read the input image file "Old-Pic.png". The cvtColor method is called on the input_image object to convert it to grayscale, and the resulting grayscale image is stored in the gray_image object.

 -  The calcHist function from OpenCV is then called on the gray_image object to calculate its histogram. The resulting histogram is stored in the hist object.

 -  The histogram is plotted using the hist function from the pyplot module in the matplotlib library. The ravel method is called on the gray_image object to convert it to a 1D array, and 256 bins are used to represent the histogram. The resulting histogram is shown using the show method.

-  The histogram is plotted using the plot function from OpenCV. The resulting histogram is shown using the show method.

*NOTE*

 that the two histograms may look slightly different due to differences in the way that the hist and plot functions calculate histograms. However, both histograms should provide a good representation of the grayscale image's pixel intensity distribution.

 ---
 [Q6. Write a program to read an image convert to gray scale then calculate and
display its histogram. Ask the user for a threshold (t) to apply the thresholding to
convert the image to binary then show the binary image. Use the program to try
different values, can you manually estimate the best threshold.]()


### description

 -  In this program, the cv2 module from OpenCV is used to read the input image file "Old-Pic.png". The cvtColor method is called on the input_image object to convert it to grayscale, and the resulting grayscale image is stored in the gray_image object.

 -  The calcHist function from OpenCV is then called on the gray_image object to calculate its histogram. The resulting histogram is stored in the hist object. The histogram is plotted using the hist function from the pyplot module in the matplotlib library.

 -  The program then prompts the user for a threshold value using the input function. The threshold value is converted to an integer using the int function.

 -  The threshold function from OpenCV is then called on the gray_image object, with the threshold value provided by the user as the threshold value. This converts the grayscale image to binary using a simple thresholding method. The resulting binary image is stored in the binary_image object.

 -  The imshow function from OpenCV is then called on the binary_image object to display the binary image. The user can experiment with different threshold values by entering different values when prompted, and the effect of the thresholding can be observed on the resulting binary image.

*NOTE*
<h4>
Determining the best threshold value for a given image is often an empirical process, and it depends on the specific characteristics of the image being processed. A common approach is to try a range of threshold values and visually inspect the resulting binary images to find the threshold that produces the best segmentation result. Another approach is to use automatic thresholding methods that aim to find the optimal threshold value based on some objective criterion, such as maximizing between-class variance or minimizing error rates.
</h4>

---
- [Q7. Repeat the previous question using automatic thresholding. . (apply this
program twice first using open cv function for automatic threshold selection and
second without using the function). Apply the function by yourself.](https://github.com/Mohamed-Silaya/Image_processing/blob/main/q7.py)

### description

 -  In this program, the cv2 module from OpenCV is used to read the input image file "Old-Pic.png". The cvtColor method is called on the input_image object to convert it to grayscale, and the resulting grayscale image is stored in the gray_image object.

 -  Automatic thresholding is applied using two methods: OpenCV's built-in threshold function with the cv2.THRESH_OTSU flag, and a custom implementation of Otsu's thresholding method. The threshold function from OpenCV is called on the gray_image object to apply automatic thresholding using Otsu's method. The resulting binary image is stored in the binary_image_cv object.

 -  For the custom implementation of Otsu's method, the otsu_threshold function takes a grayscale image as input and returns a binary image using Otsu's method. This function computes the histogram of the input image, normalizes it, and computes the cumulative sum. It then computes the mean and variance for all possible threshold values, and uses these values to compute the between-class variance for each threshold value. The optimal threshold value is chosen as the one that maximizes the between-class variance. Finally, the function applies thresholding to the input image to convert it to binary using the optimal threshold value.

 -  The histogram is plotted using the hist function from the pyplot module in the matplotlib library.

 -  The resulting binary images are displayed using the imshow function from OpenCV. The user can compare the binary images produced by the two methods and observe the differences in the segmentation results.

 ---
  [Q8. Given the following image file write a program to:](https://github.com/Mohamed-Silaya/Image_processing/blob/main/q8.py)

-  A) Apply a 3 X 3 median filter on the image
-  B)Apply a 5 X 5 median filter on the image
-  C)Apply a 3 X 3 mean (average) filter
-  D)Apply a 7 X 7 mean (average) filter
Compare the results of mean and median filter and different filter size

- ### description 

 -  In this program, the cv2 module from OpenCV is used to read the input image file "Old-Pic.png". The cvtColor method is called on the input_image object to convert it to grayscale, and the resulting grayscale image is stored in the gray_image object.

 -  The program then applies median and mean filters to the grayscale image with different filter sizes. The medianBlur function from OpenCV is used to apply median filters with a kernel size of 3x3 and 5x5. The filter2D function from OpenCV is used to apply mean filters with a 3x3 kernel and a 7x7 kernel. The results of each filtering operation are stored in a separate variable.

 -  The program then displays the original grayscale image and the filtered images using the imshow function from the pyplot module in the matplotlib library. The subplot function is used to display the images in a grid layout.

*NOTE* :
<h4>
 The results of the program can be used to compare the effects of median and mean filters with different filter sizes on the input image. Median filters are effective at removing noise and preserving edges, but they can also introduce artifacts and blur fine details. Mean filters are effective at smoothing the image and preserving global features, but they can also blur edges and details. The choice of filter size depends on the specific characteristics of the image and the desired trade-off between noise reduction and detail preservation. In general, larger filter sizes can lead to stronger smoothing and more loss of detail, while smaller filter sizes can preserve more detail but may not be as effective at removing noise.
 </h4>

---
[Q9. Given the following image file write a program to read the image and find
the resolution of this image, the bit depth of this image.](https://github.com/Mohamed-Silaya/Image_processing/blob/main/q9.py)
- Calculate and draw the histogram of the image (gray scale image).
- Calculate and draw the normalized histogram
- Calculate and draw the cumulative histogram.
- Perform histogram equalization and write the image and draw the
histogram after equalization.

 -  In this program, the cv2 module from OpenCV is used to read the input image file "Old-Pic.png". The program then retrieves the resolution and bit depth of the image using the shape attribute and the dtype attribute of the image object.

 -  The program then converts the input image to grayscale using the cvtColor method and the COLOR_BGR2GRAY flag. The grayscale image is stored in the gray_image object.

 -  The program then calculates the histogram of the grayscale image using the histogram function from NumPy. The histogram is plotted using the hist function from the pyplot module in the matplotlib library.

 -  The program then calculates the normalized histogram and cumulative histogram of the grayscale image using the hist_norm and hist_cumsum variables, respectively. The normalized histogram is plotted using the plot function from pyplot, and the cumulative histogram is also plotted using the plot function.

 -  The program then performs histogram equalization on the grayscale image using the equalizeHist function from OpenCV. The resulting equalized image is stored in the hist_equalized object.

 -  The program then displays the equalized image and its histogram using the imshow function from OpenCV and the hist function from pyplot, respectively.

*NOTE* : 
 
The results of the program can be used to analyze the characteristics of the input image and to perform various image processing operations, such as histogram equalization, to enhance the visual quality of the image.

---
[Q10. Write a program to read an image, convert it to grayscale image and
divide the image into batches (parts)](https://github.com/Mohamed-Silaya/Image_processing/blob/main/q10.py)
- The program should ask user about the
batch size. (Display and store the batches).

### description

 -  In this program, the cv2 module from OpenCV is used to read the input image file "Old-Pic.png". The program then converts the input image to grayscale using the cvtColor method and the COLOR_BGR2GRAY flag. The grayscale image is stored in the gray_image object.

 -  The program then prompts the user to enter a batch size, which is stored in the batch_size variable.

 -  The program then calculates the number of rows and columns needed to divide the image into batches of the given size using the ceil function from the math module. The batches are stored in a two-dimensional list called batches.

 -  The program then iterates over each batch, displays it using the imshow function from OpenCV, and stores it as a separate image file using the imwrite function. The batch images are named "batch_1.jpg", "batch_2.jpg", and so on, in order from left to right and top to bottom.

*NOTE* :

 The results of the program can be used to divide a large image into smaller batches for processing or analysis, or to perform batch operations on the image data.
 
 ## Author

 - [Mohamed Silaya](https://github.com/Mohamed-Silaya)
