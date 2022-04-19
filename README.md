# IOET-TEST
# Overview of the Solution
The first thing to do is read the data from the .txt file, once done that, the next step  is to storage the data the most efficient way,
which in this case is in a dictionary, with the day as key and for value the names and schedules of the employees as an inner dictionary. Storing the data in this way help us to relate the names of the employees who worked on the same day, so all we have left to do is compare the hours employees were in to find out if they were in the office together.

To do this, we have to iterate in the internal dictionaries, in which the name of the employee and the time in which he was in the office will be extracted. Then the start and end time will be compared with the other employees on that day, and they will be added to a new dictionary that will have as a key a tuple of the two employees that coincided and as a value the times they did so.
# Approach and Methodology

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
Execute the following command for the automated tests
```
py -m unittest test/test_hours.py
```
or
```
python -m unittest test/test_hours.py
```
## Autor ✒️

* **Fernando Barros** - *Developer* - [FernandoBarros12](https://github.com/FernandoBarros12)