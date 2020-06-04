from app import app
from os import environ

app.config["SECRET_KEY"] = '42ff64074324c331307ab405e5c362ca71bb9b8ecf0e58bf'

if __name__ == '__main__':
    app.run()