import click
from facial_recognition.cli.csv.create_csv import csv

@click.group()
def facerec():
    pass

facerec.add_command(csv)


if __name__ == "__main__":
    facerec()
