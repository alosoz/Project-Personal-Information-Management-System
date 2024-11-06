# Project-Personal-Information-Management-System

Project Description: In this project, we will develop a system that allows users to enter their personal information (e.g., name, age, email, address) and save it in a JSON file. Users will also be able to read and manage this information from the JSON file. This project will help you improve your skills in using functions, classes, and dynamic coding.

## Requirements:
  Python (3.x)
  JSON module (comes with Python)

## Task 1: Creating the Project Folder Structure
  1. Create the folder structure:
    Make a folder named personal_info_manager.
    Inside this folder, create a sub-folder named data.
    Inside personal_info_manager, create two Python files: main.py and personal_info.py.

## Task 2: Coding personal_info.py
  1. Defining Classes and Functions:
      Open personal_info.py
      Explanation:
          load_info(): Checks if the file exists. If it does, it loads the JSON data; if not, it             returns an empty dictionary.
          save_info(): Saves the information in JSON format to the specified file.
          add_info(): Adds new user information to the JSON data by loading, updating, and then              saving it back to the file.

## Task 3: Coding main.py
  1. Writing the Main Program:
    Open main.py
  Explanation:

      main(): Displays a menu to the user for adding information, viewing stored information,         or exiting.
      Options:
      1. Add Info: Prompts the user for name, age, email, and address, then adds this                 information using add_info().
      2. View Info: Loads and displays all saved information.
      3. Exit: Ends the program.

## Task 4: Creating the JSON File
  1. Creating an Empty JSON File:
    Inside the data folder, create an empty file named personal_info.json.

## Task 5: Running the Project
  1. Running the Program in Terminal:
    Open the terminal, navigate to the project folder (personal_info_manager)

## Task 6: Testing and Enhancing the Project
  1. Testing:
    From the menu, choose 1. Add Info to add a few entries.
    Choose 2. View Info to display the added information.
    Choose 3. Exit to quit the program.
  2. Enhancing:
     You can add more features, like deleting or updating existing information, to further           enhance   this project. By following these tasks, you will have a functional Personal           Information Management System. 

