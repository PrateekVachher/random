from tasks import factorial
dataset = []
dataset.append(factorial.delay(1,5))
'''
dataset.append(factorial.delay(100,200))
dataset.append(factorial.delay(200,300))
dataset.append(factorial.delay(300,400))
'''
while True:
    print ('PROCESSING')
    flag = 1
    for x in dataset:
        if x.ready():
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        #tot = dataset[0].get()*dataset[1].get()*dataset[2].get()*dataset[3].get()
        print (dataset[0].get())
        break
