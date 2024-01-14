import os
import random
import time

from celery import Celery
from dotenv import load_dotenv

load_dotenv()

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")

assert (
    CELERY_BROKER_URL is not None and CELERY_RESULT_BACKEND is not None
), "Celery broker URL and result backend must be set"

celery = Celery(__name__, broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@celery.task(name="add")
def add(x, y):
    time.sleep(random.randint(1, 3))
    return x + y


def start():
    celery.worker_main(argv=["worker", "--loglevel=INFO"])
