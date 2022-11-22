Project:
Cafe internal Order System

Project Background:
Create a system for making order internally when customer make a new order.
There is a main menus for selecting 3 sub-menus.
There are 3 sub-menus for manage product, order and courier.
Each menus can display, creat, update and delete the list in dictionary. 
Also, it can return to main menu for choosing to get in another menu.
It also can return to main menu and exit the app and save all the information to extra files at the same time.
If run the program again, all data is loaded and can be displayed on system.


How did you meet the client brief?
I create a "data" folder for contain 3 files to save product, coustomer and courier information separately.
Because there are a lot of information of each file and there are included key and value.
Therefore, csv file format is suitable for this situation, so that I can use dictionary to store all of those data.
For the code, there are 7 python files and save in same folder names "source".
"app.py" is the main file for running the system. It is calling a function "main_menu" from file "main_menu.py".
"main_menu.py" run the main menu to select the number to get in sub menu, so that it is calling 3 functions for each menu.
There are using typing number for selecting which menu/function has been run.
If user get in each menu, there are couple options for diffenert functions, such as display, create, update and delete.
User can type the data by following instruction and write into the file automaticly.
All sub-menu can return to main menu and exit the app.

How did you guarantee the client requirements?
I tried to write a test code for testing the function if it can run normally.
There are a lot of opeing file and read the file's data that is dictionary.


If you had more time, what is one thing you would improve upon? (ACTION PLAN FOR FUTURE IMPLEMENTATION)
What did you most enjoy implementing? (BANTS)

