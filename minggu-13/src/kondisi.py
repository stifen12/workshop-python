#program menghitung upa kerja per minggu
print("menghitung upa kerja karja karyawan perminggu")
print()
nama=(input("nama anda ="))
jkerja=int(input("masukan jam kerja ="))
upaperjam=int(input("upa per jam =RP."))
if (jkerja<=35):
upatotal=jkerja*upaperjam #if dengan kondisi diberi jarak
else:
upatotal=jkerja*upaperjam+35*upaperjam #else dengan kondisi diberi jarak
print("upa kerja anda dalam 1 minggu =RP.",upatotal)
print("----------------------------------------")
print("karyawan",nama,"menerima upa dalam 1 minggu=RP.",upatotal)