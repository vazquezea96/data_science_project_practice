# Data Science Project
## Practice project from Educatives, "Learn to Code: Become a Software Engineer" path.

### Topics Learned:
- Reading Data from a File
  - Learned how to use Python's NumPy (numpy) library. A very famous library that a lot of data scientists use. NumPy is a powerful library for numerical operations in Python. It equips us with a variety of functions and tools to implement complex mathmatical operations. For this particular project, I learned about NumPy's loadtxt() function, which can take many input arguments including a file name.
    ```
       import numpy
    
       data = numpy.loadtxt('data.txt')
       print(data)
    ```
- Dictionaries in Python
  - Another way to represent data in Python is another data structure called a Dictionary. Every entry in the dictionary has a unique word, and against each of those unique words, there's an associated definition.
  - Python's dictionary calls the unique word key and the definition a value.
   ```
    fitness_list = ["Eddie", 1000, 10000, 2000]
    key = fitness_list[0]
    value = fitness_list[1:]

    fitness_dictionary = {} # creates a dictionary literal
    fitness_dictionary[key] = value  # adds the key and values to the dictionary 
    
    ```
- Data Visualization
  - Another library Python offers us is the matplotlib. For this project, we are going to use the pyplot module from the matplotlib library. It is used for plotting in Python. Using the pyplot module, there are functions we can call in our code for plotting:
    - pie charts
    - bar charts
    - line and scattor plots
    - bubble plots
- Sorting Information
- Problem Solving--Integration

### Screen shots
#### Bar Graph Example:
![image](https://github.com/user-attachments/assets/02d3afe7-1492-434b-b7d7-4c40bbd7ed05)

![image](https://github.com/user-attachments/assets/85715e1e-1793-45cf-a692-e479b38ce65e)

