# Duplicate Image Finder

Many a times, we find duplicate images residing in our Albums, Image_directory etc, there ane various reasons, 
downloading same file form various sources, auto  backup on cloud, it slipped out of our mind that we downloaded it 
already in the first place etc. Manually selecting them is actually a hassle, but why do such boring task when 
automation can do the trick. This sweet and simple script, helps you to compare various files (not only images) in a 
directory, find the duplicate, list them out, and then even allows you to delete them. 
**Sweet!!!**

## Setup

- Setup a `python 3.x` virtual environment.
- `Activate` the environment
- Install the dependencies using ```pip3 install -r requiremnts.txt```
- You are all set and the [script](image_finder.py) is Ready to run.
- Clearly Follow the Instructions provided in the comments.

### Usage
In Command Line Interface, Run the script using -

`python image_finder.py <path of folder1, path  of folder2, .....>`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. folder1 - *Parent Folder*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. folder2, folder3 .... - *Subsequent Folders*
        
>Comparisons are done with in the folder, and from Parent to Subsequent Folders.

## Dependencies
 1. python3
 2. keyboard

## Detailed explanation

The Script works on a simple fundamental. Two files with same [`md5checksum`](https://en.wikipedia.org/wiki/MD5) will 
have similar contents. So in the script all we aim to do is determine the checksum, compare and find the duplicates.

#### Folder Structure

- **[Stand_Alone](./Stand_Alone)** folder has 6 images, 2 of them are duplicate of images within the folder only.
- **[Parent](./Parent)** contains standard images used for Image Processing in *png* format.
- **[Duplicate](./Duplicate)** folder contains 5 images duplicate of images in Stand_Alone (named `Random Name (n)`).
There are similar images in *tiff* extension as well, They are not Duplicate as file type is different.
- **[Duplicate_1](./Duplicate_1)** folder contains another 5 images duplicate of images in Stand_Alone 
(named `Another Random Name (n)`). There are similar images in *jpeg* extension as well, They are not Duplicate as file 
type is different.

## Output

## Author(s)

Made by [Vybhav Chaturvedi](https://www.linkedin.com/in/vybhav-chaturvedi-0ba82614a/)

Check [Rotten Scripts](https://github.com/HarshCasper/Rotten-Scripts) for more explanation and Implementation