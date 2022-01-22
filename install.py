import os
from sys import platform
if platform == "linux" or platform == "linux2":
    os.system('pip install shutil')
    os.system('pip install Pillow')
    os.system('pip install imageio')
elif platform == "darwin":
    os.system('pip install shutil')
    os.system('pip install Pillow')
    os.system('pip install imageio')
elif platform == "win32":
    # Windows...
    os.system('cmd /k "pip install shutil"')
    os.system('cmd /k "pip install Pillow"')
    os.system('cmd /k "pip install imageio"')
print("Done")