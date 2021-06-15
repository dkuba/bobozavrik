from apscheduler.schedulers.background import BackgroundScheduler
from . import jobs_1    


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(jobs_1.add_new_ad, 'interval', days=7)
    scheduler.start()


