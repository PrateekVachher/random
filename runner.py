from tasks import add
dataset = []
for x in range(1,100):
    dataset.append(factorial.delay(1,1000))
    dataset.append(factorial.delay(1000,2000))
    dataset.append(factorial.delay(2000,3000))
    dataset.append(factorial.delay(3000,4000))
while True:
    print 'PROCESSING'
    flag = 1
    for x in dataset:
        if x.ready():
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        tot = dataset[0].get()+dataset[1].get()+dataset[2].get()+dataset.get()
        print tot
        break
