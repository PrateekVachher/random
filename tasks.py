from celery import Celery
broker_url = 'amqp://myuser:mypassword@54.69.82.183:5672/myvhost'
backend_url = 'rpc://myuser:mypassword@54.69.82.183:5672/myvhost'
app = Celery('tasks', broker=broker_url, backend = backend_url)

@app.task
def factorial(x,y):
    mul = 1
    for x1 in range(x,y):
        mul*=x1
    return mul