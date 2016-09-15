from facial_recognition.constants import USER_DATA_DIRECTORY
from facial_recognition.core.person_info import get_person_info, PersonNotFoundException
import click
import cv2
import os


@click.command()
@click.option('--name', prompt='Enter new person name')
@click.option('--csv', help="CSV file to use")
def add(name, csv):
    with get_person_info(csv) as people:
        try:
            person = people.get(name=name)
            id = person['id']
        except PersonNotFoundException:
            click.echo("No person " + name + " found.")
            id = click.prompt("Enter an id number if you know it," +
                               " otherwise a new person will be created", default=-1,
                               type=int, show_default=False)
            try:
                if id is not None:
                    person = people.get(id=id)
            except PersonNotFoundException:
                if id >= 0:
                    click.echo("Person with id " + str(id) + " was not found")
                info = click.prompt("Write some information about this person to add")
                people.add(name, info)

    try:
        os.mkdir(USER_DATA_DIRECTORY)
    # dir already exists
    except OSError:
        pass
    pictures_dir = os.path.join(USER_DATA_DIRECTORY, 'pics')
    try:
        os.mkdir(pictures_dir)
    # dir already exists
    except OSError:
        pass
    this_person_dir = os.path.join(pictures_dir, str(id))
    try:
        os.mkdir(this_person_dir)
    # dir already exists
    except OSError:
        pass
    if click.confirm("Take picture of  " + name + "?"):
        video_capture = cv2.VideoCapture(0)
        ret, frame = video_capture.read()
        file_name = 'subject{}.jpg'
        file_number = 0
        while os.path.isfile(os.path.join(this_person_dir, file_name.format(file_number))):
            file_number += 1
        cv2.imwrite(os.path.join(this_person_dir, file_name.format(file_number)), frame)
