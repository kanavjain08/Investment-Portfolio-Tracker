import requests
from website import create_app
from bs4 import BeautifulSoup

app = create_app()

# runs the web server iff you run this file
if __name__ == '__main__':
    app.run(debug = True)

