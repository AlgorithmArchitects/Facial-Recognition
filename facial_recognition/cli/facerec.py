import click
from facial_recognition.cli.recognize.recognize import recognize
from facial_recognition.cli.train.train import train
from facial_recognition.cli.add.add import add


@click.group()
def facerec():
    pass

facerec.add_command(recognize)
facerec.add_command(train)
facerec.add_command(add)


if __name__ == "__main__":
    facerec()
