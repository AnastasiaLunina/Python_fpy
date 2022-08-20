# Homework 1.«Import. Module. Package»

1. Make a structure of "Accounting" program. 
- main.py;  
- directory application:  
-- salary.py;  
-- directtory db:  
\--- people.py;  
main.py - main module for program execution.  
In module salary.py create function calculate_salary.  
In module people.py create function get_employees.  

2. Import functions to module main.py and call those functins in following construction.
```
if __name__ == '__main__':
```

3. Learn about module [datetime](https://pythonworld.ru/moduli/modul-datetime.html). 
When call the functions in module main.py print current date.

\*4. Create module dirty_main next to module main.py and import all functions with construction (optinal)
```
from package import *
```
