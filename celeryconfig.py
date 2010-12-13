CELERY_RESULT_BACKEND = "database"
CELERY_RESULT_DBURI = "sqlite:///celerydb.sqlite"

BROKER_BACKEND = "sqlakombu.transport.Transport"
BROKER_HOST = "sqlite:///celerydb.sqlite"

CELERY_IMPORTS = ("tasks",)

