import click
from facial_recognition.cli.recognize.recognize import recognize
from facial_recognition.cli.train.train import train


@click.group()
def facerec():
    pass

facerec.add_command(recognize)
facerec.add_command(train)


if __name__ == "__main__":
    facerec()
