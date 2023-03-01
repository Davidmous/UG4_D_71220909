print("="*10,"BARIS ARITMATIKA","="*10)

a = int(input("Masukan bilangan awal >>> "))
b = int(input("Masukan selisih bilangan >>> "))
n = int(input("Masukan banyaknya suku >>> ")
        )
def aritmatika(a,b,n) :
    deret = n/2 * (2*a  + (n -1) * b)
    return deret

print("Total dari deret aritmatika tersebut adalah : ",aritmatika(a,b,n))