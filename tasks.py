from celery.decorators import task

@task
def tambah(a, b):
    return a + b

