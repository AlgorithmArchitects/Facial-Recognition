from facial_recognition.constants import USER_DATA_DIRECTORY
from contextlib import contextmanager

import os
import pandas

DEFAULT_CSV_LOC = os.path.join(USER_DATA_DIRECTORY, 'person_info.csv')


class PersonInfo(object):
    """
    A class for interacting with the person info csv

    Use get_person_info to ensure that the file is properly saved when
    you are finished with it
    """
    fields = ['id', 'name', 'info']

    def __init__(self, csv_path=None):
        if csv_path is None:
            try:
                os.mkdir(USER_DATA_DIRECTORY)
            # dir already exists
            except OSError:
                pass
            csv_path = DEFAULT_CSV_LOC

        self.csv_path = csv_path

        try:
            self.dataframe = pandas.read_csv(self.csv_path, names=self.fields)
        except (IOError, pandas.io.common.EmptyDataError):
            self.dataframe = pandas.DataFrame(columns=self.fields)

        self.dataframe = self.dataframe.set_index(['id'])

    def add(self, id, name, info):
        self.dataframe = self.dataframe.append([[id, name, info]])

    def get(self, id):
        """
        Returns a dict of a person (keys: id, name, info)
        Raises a KeyError if it's not there
        """
        row = self.dataframe.loc[[id]].to_dict()
        person = {'id': id, 'name': row['name'][id], 'info': row['info'][id]}
        return person

    def close(self):
        self.dataframe.to_csv(self.csv_path, index=False)



@contextmanager
def get_person_info(csv_path=None):
    """
    A context manager for interacting with PersonInfo.

    Usage:

    from facial_recognition.core.person_info import get_person_info

    with get_person_info() as person_info:
        # use person_info as an instance of PersonInfo
    """
    info = PersonInfo(csv_path)
    try:
        yield info
    finally:
        info.close()
