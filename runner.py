from tasks import add
dataset = []
for x in range(1,100):
    dataset.append(add.delay(x,x))
