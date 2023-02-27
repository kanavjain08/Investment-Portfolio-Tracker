from website import create_app

app = create_app()

# runs the web server iff you run this file
if __name__ == '__main__':
    app.run(debug = True)

