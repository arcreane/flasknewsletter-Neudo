from OurApp import app, csrf


if __name__ == "__main__":
    app.run()
    csrf.init_app(app)