import click
from facial_recognition.cli.csv.create_csv import csv
from facial_recognition.cli.webcam.webcam import webcam


@click.group()
def facerec():
    pass

facerec.add_command(csv)
facerec.add_command(webcam)


if __name__ == "__main__":
    facerec()
