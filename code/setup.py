import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":base="Win32GUI"

exe=Executable(script="mnist-classifier.py",base=base)

setup(name='mnist-calsifier.py',
      version='0.1',
      description='手書き文字を判別します',
      excutable=[exe])
