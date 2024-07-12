import os
apath = "C:\\Users\\tr\\Desktop\\python2\\dosyaislemleri\\dosyalar\\yeni.txt"
rpath = "dosyaislemleri\\dosyalar\\yeni.txt"

# # if os.path.exists(apath):
# #     print("evet dosya mevcut")
# # else:
# #    print("dosya mevcut deeel")

# # dosya = open(apath,"r" ,encoding="utf-8")
# # icerik = dosya.read()
# # print(dosya.tell())

# icerik = dosya.read(5)
# print(icerik)
# print(dosya.tell())

#
#icerik = dosya.readlines()       #readlines hepsını satır satır okuyup yazdırıyor
#print(icerik)
#dosya.close(



dosya = open(apath "w",encoding="u)
data=["birinci satir","ikicni satir" "ücüncü satir"] 
print(dosya.tell())
dosya.flush()