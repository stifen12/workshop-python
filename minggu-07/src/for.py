y = [10,20,30,40,50,60,70,80,90]
for x in y:
    if x==50:
        continue
    if x>70:
        break
    print x
else:
    print 'Perulangan selesai'