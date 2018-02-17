from celery import Celery
broker_url = 'amqp://myuser:mypassword@128.101.53.68:5672/myvhost'
backend_url = 'rpc://myuser:mypassword@128.101.53.68:5672/myvhost'
app = Celery('tasks', broker=broker_url, backend = backend_url)

@app.task
def add(x, y):
    return x + y