# Terminal Record: Ridgeline Tool Rental

## 1. Building The Project
```bash
mkdir ism3232-midterm
cd ism3232-midterm
pwd
python3 -m venv .venv
source .venv/bin/activate
python3 -m install pytest ruff
pthon3 -m pip freeze > requirements.txt
pwd
touch business_rules.py main.py commands.md README.md .gitignore
mkdir tests
cd tests
pwd
touch __init__.py test_business_rules.py
cd ..
tree
ll
git status
git add .
git status
git commit -m "Created the folder, files and structure"
git push -u origin main
```
## 2. The virtual environment

I used this command to see if i'm in the virtual environemnt 

```bash


which python3
```
```
/Users/sebastiancooper/ism3232-midterm/.venv/bin/python3

```
My output here shows that I am working in the virtual environment

## 3. The Project Structure

I ran this to show the outline of my folders
```bash
tree -L 2
```
```
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```
With the output you can see that I have all of my files for the midterm

## 4. Every function and test
I run this to see all the functions that I defined
```bash 
rg 'def '
```
```
business_rules.py
18:def calculate_rental_cost(daily_rate: float, days: int) -> float:
23:def get_rental_discount(days: int, contractor: bool = False) -> float:
36:def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
46:def requires_deposit(quote: float) -> bool:
51:def needs_inspection(days: int, quote: float) -> bool:
56:def total_quoted(rentals: list) -> float:
69:def largest_rental(rentals: list) -> str:
85:def format_rental_line(

tests/test_business_rules.py
13:def test_calculate_quote_as_false():
17:def test_calculate_quote_as_true():
21:def test_calculate_rental_cost_at_70():
25:def test_calculate_rental_cost_at_60():
29:def test_calculate_rental_cost_at_85():
33:def test_get_rental_discount_as_false1():
37:def test_get_rental_discount_as_true2():
41:def test_get_rental_discount_as_false8():
45:def test_get_rental_discount_as_true6():
49:def test_format_rental_line_Alvarez():
56:def test_format_rental_line_Brennan():
63:def test_format_rental_line_Chowdhury():
70:def test_largest_rental():
79:def test_needs_inspection_as_false():
83:def test_needs_inspection_as_true():
87:def test_requires_deposit_as_false():
91:def test_requires_deposit_below_threshold():
95:def test_requires_deposit_at_threshold():
99:def test_total_quoted():
108:def test_largest_rental_empty_list():
```
This shows my 8 business rules and my 23 pytest functions

## 5. Which file prints

Running this shows me what files print 
```bash 
rg -l print
```
```
main.py
commands.md
```
With this output both main.py and commands.md contain print so they are shown above.

## 6. The commit history
Running this show my commit history so far this project
```bash
git log --oneline
```
```
213b1f4 (HEAD -> main, origin/main) Finished test_business_rules.py
fa77a37 fixed python formating
8492c35 Finished section 3 the main.py
8ee0b08 finished all 8 ruled and ran which python3 in the terminal
79eca3f Worked on the calculate rental cost function, the get_rental_discount, constants, and commands.md
c76c4b0 Created the folder, files and structure
```
Here are all 6 of my commits and my messages throughout this project