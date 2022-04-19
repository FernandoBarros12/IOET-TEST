# IOET-TEST
# Overview of the Solution
The first thing to do is read the data from the .txt file, once done that, the next step  is to storage the data in the most efficient way, which in this case is in a dictionary, with the day as key and the names and schedules of the employees in an inner dictionary as value. Storing the data in this way help us to relate the names of the employees who worked on the same day, avoiding to use an extra iterator to compare this value, so all we have left to do is compare the hours employees were in to find out if they were in the office together.

To do this, we have to iterate in the internal dictionaries, in which the name of the employee and the time in which he was in the office will be extracted. Then the start and end time will be compared with the other employees on that day, and they will be added to a new dictionary that will have as a key a tuple of the two employees that coincided and as a value the times they did so.
# Approach and Methodology
For this test I use the OOP paradigm because of its advantages when it comes to modify the code and protect the data used, to ensure the quality of the code I used pylint, which establishes generalized rules when coding and allows an easier reading for the developer by implementing the best practices in coding standards. In addition, I use screaming architecture for a better project organization which helps other developers to understand the code.
I choose the iterator desing pattern because it is the one that best fit the exercise because I had to use iterators to go through the information provided by the user and to storage that information I use dictionaries because of their Key-Value structure which will come handy later in the development of the exercise, I have a main file in which all the methods will be called. 



# Execution
Open a terminal and go to the directory 
```
cd IOET-TEST
```
Execute the main file using the following command
```
py src/main.py 
```
or
```
python src/main.py 
```
# Running the test
I have made automated tests using Unittest which will evaluate the input in a core function of the programm. The first test will compare stablished time values with the ones used in the programm to make sure that the hour formatting function is working correctly.
The second test will raise a Type error in case the argument pass to the function is not a String.

Execute the following command for the automated tests
```
py -m unittest test/test_hours.py
```
or
```
python -m unittest test/test_hours.py
```
# Built With
Python 3.10
## Autor ✒️

* **Fernando Barros** - *Developer* - [FernandoBarros12](https://github.com/FernandoBarros12)