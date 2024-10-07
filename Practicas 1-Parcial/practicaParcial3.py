# -1 + 1/2! - 1/3! + 1/4! - 1/5!
suma=-1
factorial=1
signo=1
for i in range(2,6):
    factorial*=i
    t=((-1)**i)*(1/factorial)
    
    suma+=t
    print(suma)