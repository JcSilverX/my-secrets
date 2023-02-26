"""
    application entry point.
"""

import getpass
import datetime

from flask.cli import FlaskGroup

from example import app, db, User

cli = FlaskGroup(app)


@cli.command('create_admin')
def create_admin():
    """
        creates admin user
    """
    firstname = str(input('enter your name: '))
    email = str(input('enter your email: '))
    password = getpass.getpass('Enter password: ')
    confirm_password = getpass.getpass("Enter password again: ")

    if firstname == "":
        firstname = 'admin'
    if email == "":
        email = 'admin@admin.com'
    if password == "":
        password = 'admin123'
    if confirm_password == "":
        confirm_password = 'admin123'

    if password != confirm_password:
        print('passwords don\'t match')
    else:
        try:
            db.session.add(User(
                    first_name=firstname,
                    email=email,
                    password=password,
                    is_admin=True,
                    is_confirmed=True,
                    confirmed_on=datetime.datetime.now()
                )
            )
            db.session.commit()
            print(f'admin with email {email} was created successfully!')
        except Exception:
            print("couldn't create admin user.")


if __name__ == "__main__":
    cli()

