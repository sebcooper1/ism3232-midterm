# Part 1
mkdir ism3232-midterm
cd ism3232-midterm
pwd
python3 -m venv .venv
source .venv/bin/activate
python3 install pytest && ruff
-m pip freeze > requirements.txt
pwd
touch business_rules.py main.py commands.md README.md .gitignore
mkdir tests
cd tests
pwd
touch __init__.py test business rules.py
cd ..
tree
ll
git status
git add .
git status
git commit -m "Created the folder, files and structure"
git push -u orgin main

# Part 2
