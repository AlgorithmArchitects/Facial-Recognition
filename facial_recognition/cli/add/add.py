from facial_recognition.core.person_info import get_person_info, PersonNotFoundException
import click


@click.command()
@click.option('--name', prompt='Enter new person name')
@click.option('--csv', help="CSV file to use")
def add(name, csv):
    with get_person_info(csv) as people:
        try:
            person = people.get(name=name)
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
