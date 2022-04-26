### Date created
On April 26th, 2022.

### Bike Share Project

#### Description
This project is about providing some statistics for a bike rental service, which serves in the metropolitan area of Chicago, New York City and Washingtion D.C.

The original project was designed for the completion of a course project in the "Introduction to Programming with Python for Data Science" nanodegree program of the Udacity platform.

The project is designed with a simple user interface on terminal. It basically asks the user which city they would like to see the statistics from, and some filters to limit the demographic of the computed statistic.

### Files Used

#### Data Files

There are three csv data files, one separate file for the data of each city. All datasets are already preprocessed and prepared for computing the statistics by the Udacity's relevant curriculum developed team. Notice that the original data is derived from many different distributed data sources. However, I won't include the data files here due to copyright reasons.

#### Source Code Files

There is a single source code file in this project, a file named "bikeshare.py". It basically includes a set of functions, each for a different set of statistics. The code mostly follows the initial template, provided by the Udacity instructors. I defined an additional function for displaying a set of rows for the end user, 5 rows at a time.

### Running Instructions

Should you need to run this script, provided the respective data files, all you have to do is to change your working directory to the source code file's folder; then, type "python bikeshare.py" in the terminal. Notice that the csv data files should be in the same folder as the folder of the script file.

#### Requirements

- python 3.6.13
- pandas 1.1.5
- numpy 1.19.5
