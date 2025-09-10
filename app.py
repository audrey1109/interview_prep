'''
app.py - audrey palmer

allows for the user to run
    'python app'
in the terminal and have the website appear on the testing server
'''

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug = True)