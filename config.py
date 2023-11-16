import subprocess

def install(package):
    try:
        import pandas as pd
    except ImportError:
        print(f"Installing {package}...")
        subprocess.run(['pip', 'install', package])
    else:
        pass
        #print(f"{package} is already installed.")

fname = 'Nabat'
lname = 'Gasimzada'
allowed_pattern = r'[ a-zA-Z0-9!#%*()-=+:;"\',.?öğıəçşü]'
inf = float('inf')
min_word_limit = 5 # 0 if you don't wanna set lower limit
max_word_limit = 50 # inf if you don't wanna set upper limit
def get_score():
    pass
def install_requirements():
    pass