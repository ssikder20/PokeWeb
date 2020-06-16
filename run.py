from app import app
from os import environ
from flask_apscheduler import APScheduler

if __name__ == '__main__':
    scheduler = APScheduler()
    scheduler.add_job(func=gen_update, trigger='interval', id='job', seconds=604800)
    scheduler.start()
    app.run()