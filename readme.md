python -m venv venv

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser   

python -m pip install --upgrade pip

pip install selenium webdriver-manager pandas openpyxl python-dotenv

pip freeze > requirements.txt