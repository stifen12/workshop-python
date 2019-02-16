#Program Menghitung Nilai Akhir Siswa
#oleh Okky Rizki Rohayat, NIM: 3215101398
print()
print()


NSL=[]
NAL=[]
KetL=[]
totNA, totNB, totNC, totND, totNE=0,0,0,0,0

kond='y'
while kond=='y':
    NS=input('Nama Siswa:')
    if NS=='x':
        break
    Q=float(input('Nilai Quiz:'))
    UTS=float(input('Nilai UTS:'))
    UAS=float(input('Nilai UAS:'))
    nilai=round((Q+UTS+UAS)/3) #Round adalah fungsi untuk membulatkan angka, agar tidak ada koma
    if nilai<55:
        ket='E'
        totNE +=1
    elif 55<=nilai and nilai<60:
        ket='D'
        totND +=1
    elif 60<=nilai and nilai<70:
        ket='C'
        totNC +=1
    elif 70<=nilai and nilai<80:
        ket='B'
        totNB +=1
    else:
        ket='A'
        totNA +=1


    NSL.append(NS)
    NAL.append(nilai)
    KetL.append(ket)

print()
print()
print()
print('\t','\t','Program Menghitung Nilai Akhir Siswa')
print('\t','\t','\t','\t','oleh')
print('\t','\t','\t',' Okky Rizki Rohayat')
print('\t','\t','\t',' NIM: 3215101398')
print()
print()
print()
print('No.','\t','Nama Siswa ','\t','Nilai Akhir   ','\t','Keterangan','\t')
print()

for j in range(len(NSL)):
    print(j+1,'\t',NSL[j],'\t','\t',NAL[j],'\t','\t',KetL[j])

print()
print('Total Siswa=',len(NSL))
print('Total Nilai A=', totNA)
print('Total Nilai B=', totNB)
print('Total Nilai A=', totNC)
print('Total Nilai A=', totND)
print('Total Nilai A=', totNE)
