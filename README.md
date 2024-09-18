# MasterSign

## Prerequisites:
```bash
  Django==3.2.6
  numpy==1.23.0
  plotly==5.9.0
  requests==2.28.1

## Project Installation:
**STEP 1:** Clone the repository from GitHub.
```bash
https://github.com/HappyBiningu/MasterSign.git

**STEP 2:** Change the directory to the repository.
```bash
  cd SLR
```

**STEP 3:** Create a virtual environment
(For Windows)
```bash
  python -m venv virtualenv
```
(For MacOS and Linux)
```bash
  python3 -m venv virtualenv
```

**STEP 4:** Activate the virtual environment.
(For Windows)
```bash
  virtualenv\Scripts\activate
```
(For MacOS and Linux)
```bash
  source virtualenv/bin/activate
```

**STEP 5:** Install the dependencies.
```bash
  pip install -r requirements.txt
```

**STEP 6:** Migrate the Django project.
(For Windows)
```bash
  python manage.py migrate
```
(For MacOS and Linux)
```bash
  python3 manage.py migrate
```

**STEP 7:** Run the application.
(For Windows)
```bash
  python manage.py runserver
```
(For MacOS and Linux)
```bash
  python3 manage.py runserver
```
