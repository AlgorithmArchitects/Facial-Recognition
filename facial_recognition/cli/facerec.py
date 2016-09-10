import click
from facial_recognition.cli.csv.create_csv import csv
from facial_recognition.cli.recognize.face_recognizer import recognize


@click.group()
def facerec():
    pass

facerec.add_command(csv)
facerec.add_command(recognize)


if __name__ == "__main__":
    facerec()
