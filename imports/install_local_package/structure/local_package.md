# To setup a local package that can be installed with pip we need:
    - setup.cfg
    - setup.py

# Command:
python -m pip install -e .


# After that it can be used with the following import command:
from structure import <whatever-you-need-from-the-package>
