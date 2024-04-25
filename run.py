import os
from sys import exit
from apps import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
