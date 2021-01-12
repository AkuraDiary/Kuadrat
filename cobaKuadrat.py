#### menyelesaikan persamaan kuadrat dengan rumus kuadrat
from math import sqrt

def Diskriminan(a,b,c):
    res = b**2 - (4*a*c)
    return res

def kuadrat(a,b,c):
    D = Diskriminan(a,b,c)

    print("Diskriminan : ",D)
    #if D<0:
    #    print("akar akarnya bukan bilangan real")
    try:
        x_1 = (-b + sqrt(D)) / (2*a)
        x_2 = (-b - sqrt(D)) / (2*a)
        print("X 1 : ", x_1)
        print("X 2 : ", x_2)
    except ValueError:
        print("tidak memiliki akar real")

while True:
    a, b, c = input("\nmasukkan a b c sesuai urutan : ").split()
    #print("\n")
    #if a or b or c == "stop":
    #    break
    
    kuadrat(int(a),int(b),int(c))
        #input()



