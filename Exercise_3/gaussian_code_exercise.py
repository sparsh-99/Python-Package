#!/usr/bin/env python
# coding: utf-8

# # Gaussian Code Exercise
# 
# Read through the code below and fill out the TODOs. You'll find a cell at the end of the Jupyter notebook containing unit tests. After you've run the code cell with the Gaussian class, you can run the final cell to check that your code functions as expected.
# 
# This exercise includes a file called 'numbers.txt', which you can see if you click on the 'Jupyter' icon at the top of the workspace and then go into the folder titled 3.OOP_code_gaussian_class. The 'numbers.txt' file is read in by the read_data_file() method. There is also a solution in the 3.OOP_code_gaussian_class folder in a file called answer.py.

# In[8]:


import math
import matplotlib.pyplot as plt

class Gaussian():
    """ Gaussian distribution class for calculating and 
    visualizing a Gaussian distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
            
    """
    def __init__(self, mu = 0, sigma = 1):
        
        self.mean = mu
        self.stdev = sigma
        self.data = []


    
    def calculate_mean(self):
    
        """Method to calculate the mean of the data set.
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """       
        avg = 1.0 * sum(self.data)/len(self.data)
        self.mean = avg
        return self.mean
                


    def calculate_stdev(self, sample=True):

        """Method to calculate the standard deviation of the data set.
        
        Args: 
            sample (bool): whether the data represents a sample or population
        
        Returns: 
            float: standard deviation of the data set
    
        """
        
        #   The sample variable determines if the data set contains a sample or a population
        #   If sample = True, this means the data is a sample. 
        #   Keep the value of sample in mind for calculating the standard deviation
        #
        #   Make sure to update self.stdev and return the standard deviation as well 
        
        if sample:
            n = len(self.data)-1
        else:
            n = len(self.data)
            
        sigma = 0
        
        for i in self.data:
            sigma += (i - self.mean)**2
        sigma = math.sqrt(sigma/n)
        
        self.stdev = sigma
        return self.stdev

    def read_data_file(self, file_name, sample=True):
    
        """Method to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute. 
        After reading in the file, the mean and standard deviation are calculated
                
        Args:
            file_name (string): name of a file to read from
        
        Returns:
            None
        
        """
        
        # This code opens a data file and appends the data to a list called data_list
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()
    
        
        self.data = data_list
        self.mean = self.calculate_mean()          #self also works for method
        self.stdev = self.calculate_stdev(sample)
                
        
    def plot_histogram(self):
        """Method to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        plt.hist(self.data)
        plt.title('Historgram of the data')
        plt.xlabel('Data')
        plt.ylabel('Count')
        
                
        
    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        return (1.0 / (self.stdev*math.sqrt(2*math.pi)))*math.exp(-0.5*((x-self.mean)/self.stdev)**2)        

    def plot_histogram_pdf(self, n_spaces = 50):

        """Method to plot the normalized histogram of the data and a plot of the 
        probability density function along the same range
        
        Args:
            n_spaces (int): number of data points 
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        
        

        min_range = min(self.data)
        max_range = max(self.data)
        
         # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y


# In[9]:
gaussian_one = Gaussian()
gaussian_one.read_data_file('numbers.txt')

print(gaussian_one.mean)
print(gaussian_one.stdev)

gaussian_one.plot_histogram()

gaussian_one.plot_histogram_pdf()
