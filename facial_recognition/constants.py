import os

INCLUDES_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'includes')
USER_DATA_DIRECTORY = os.path.join(os.path.expanduser('~'), '.facerec')
DEFAULT_PICTURES_DIRECTORY = os.path.join(USER_DATA_DIRECTORY, 'pics')

