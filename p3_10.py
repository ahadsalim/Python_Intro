n= int(input('how many laptops: '))
laptops=[]
for i in range(n) :
    price = int (input('price of laptop: '))
    quality= int (input('quality of laptop: '))
    laptop=[price,quality]
    laptops.append(laptop)
status=False
for j in range(len(laptops)) :
    max_price=max(laptops)
    if not status :
        for x in laptops:
            if x[1] > max_price[1] :
                print ("happy irsa")
                status=True
                break
        laptops.remove(max_price)

if not status :
    print ('poor irsa')