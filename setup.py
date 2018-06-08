#setup.py
from distutils.core import setup
import py2exe
setup(
    console=['num_extention.py'],
    options = {
        'py2exe': {
            'packages': ['openpyxl']
#            'packages': ['os']

        }
    }
)
