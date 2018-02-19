from tasks import save_find_faces
dataset = []
for x in listdir('./pictures/'):
    save_find_faces.delay('pictures/'+x)

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
        print 'Images Classified'
        break