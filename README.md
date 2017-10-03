Cours IFT-1004 ULAVAL QRCode Validation Backend
====

# Wait a minute...

Instead of doing it manually, note that the following parts (1 and 2) about the virtual environment setup can be drastically simplified by using the built-in mechanism of your preferred IDE (e.g. Pycharm).

# 1. Create a virtual environment
```python -m venv [VIRTUAL_ENV_NAME]```

Ex: ```python -m venv venv```

PS: Note that you can use the virtualenv package if you want.

# 2. Activate the virtual env

## macOS/Linux

```source [PATH_TO_YOUR_VIRTUAL_ENV]/bin/activate```

Ex: ```source venv/bin/activate```

## Windows
```[PATH_TO_YOUR_VIRTUAL_ENV]\Scripts\activate.bat```

Ex: ```venv\Scripts\activate.bat```

# 3. Install project dependencies via pip
```pip install -r requirements.txt```

# 4. Execute the main file
```python main.py```

Enjoy !
