# ISM3232 Midterm: [the business name]

- **Name:** Sebastian Cooper
- **Version:** ALPHA
- **Date:** 08/24/26

## What This Program Does
This is a program for Ridgeline Tool Rentals. It consists of their rules and their main python script that executes the commands. 

## Business Rules

1. Calculating rental cost is daily rate multiplied by the number of days
2. Fewer than 3 days is a discount of 0% if you have a rental for 3 through 6 days your discount is 10% and if you have a rental for 7 or more days you get a discount of 20%
3. Not matter what contractors get a discount of 10% however they get the 20% if they rent for 7 or more days just like non-contractors
4. If the discounted cost is below $150 a $25 dollar damage waiver fee is added 
5. If the quote is $1000 or more you are required to deposit 
6. If a rental is more than $800 and it runs 5 days or more it is required to have a pickup inspection 

## How to Run
1. Create virtual environment
    python3 -m venv .venv
2. Activate the virtual environment
    source .venv/bin/activate
3. Install required packages
    python3 -m pip install -r requirements.txt
4. Run the code
    python3 main.py

## How to Test
Run all tests
    pytest -v
Check for errors in the code
    ruff check .
Check and make sure that the code is properly formatted
    ruff format .
## Files in This Repository
1. business_rules.py - contains the 8 different functions that calculate the business rules.
2. main.py - the main file that runs the program and prints the rental report
3. test_business_rules.py - contains all the tests that confirm that the program is working correctly 
4. __init__.py - tells python that the tests folder is a python package
5. requirements.txt - everything that is required to download 
6. .gitignore - tells what files that github should ignore and not be uploaded into my repository
7. commands.md - records the terminal commands used to test and create the project
8. README.md - explains my project and everything that it contains

## AI Use Statement
I did not use AI on this project.