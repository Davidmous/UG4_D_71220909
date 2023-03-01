masuk = eval(input("Masukan sekumpulan bilangan (pisahkan dengan koma) : ").split(","))
# list = []
# for i in masuk :
#     list.append(masuk)
a = masuk
ooo = lambda a : max(a)
print("Bilangan terbesar dari bilangan di input adalah",ooo(masuk))
eee = lambda a : min(a)
print("Bilangan terkecil dari bilangan di input adalah",eee(masuk))




