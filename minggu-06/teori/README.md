
Penanganan error


Cara Menangani Exceptions di Python

Sangat lumrah untuk mengalami error selama eksekusi dari sebuah program. Dua macam error yang lumrah dan perlu ditangani adalah syntax error dan exceptions. Syntax error terjadi ketika kamu mengetik kode-nya dengan salah. dalam beberapa kasus, baris yang keliru diulangi oleh parser-nya dengan sebuah panah menunjuk ke lokasi terkini di mana error-nya terdeteksi.

Excepetions berbeda dengan syntax error. mereka terjadi selama eksekusi sebuah program saat sesuatu yang tidak diperkirakan terjadi. contohnya, mari katakan kamu meminta penggunanya untuk memasukkan sebuah angka untuk melakukan sebuah pembagian. Sekarang, jika penggunanya memasukkan sebuah string ketimbang sebuah angka dan kamu mencoba membagi sebuah angka dengan input yang diberikan, program-nya akan mengeluarkan TypeError,

Ketika tidak menangani exceptions dengan tepat, program-nya akan keluar secara paksa karena dia tidak tahu apa yang perlu dilakukan dalam kasus tersebut. Kode berikut adalah sebuah contoh:

keep_asking = True
 
while keep_asking:
    x = int(input("Enter a number: "))
    print("Dividing 50 by", x,"will give you :", 50/x)
Sepanjang kamu memasukkan nilai input integral, programnya akan bekerja dengan benar. Walau bagaimanapun, sesegara kamu memasukkan sebuah string atau bahkan sebuah angka desimal sebagai masukannya, kamu akan menerima exception ValueError.

Pada panduan ini, kamu akan belajar cara menanganinya dengan tepat dan mengankat exceptions di Python.

Beberapa Exceptions yang Umum
Berikut adalah beberapa exceptions dasar yang mungkin kamu alami saat menulit program. Kamu bisa baca lebih banyak mengenai built-in exceptions di situs resminya.

NameError: exception ini muncul ketika program-nya tidak dapat menemukan sebuah nama lokal atau global. Nama yang tidak dapat ditemukan dimasukkan ke dalam pesan error-nya.
TypeError: Pengecualian ini muncul ketika sebuah fungsi dilewatkan ke sebuah objek dari tipe yang tidak tepat sebagai sebuah argumen. Detil lengkapnya disediakan melalui pesan error.
ValueError: Pengecualian ini terjadi ketika sebuah fungsi argumen memiliki tipe yang benar namun nilai yang salah.
NotImplementedError: Pengecualian ini muncul ketika sebuah objek seharusnya mendukung sebuah operasi namun belum diterapkan. Kamu seharusnya tidak menggunakan error ini ketika fungsi yang diberikan tidak ditujukan untuk mendukung tipe dari argumen masukan-nya. Pada situasi tersebut, memunculkan TypeError exception jauh lebih tepat.
ZeroDivisionError: Exception ini muncul ketika kamu menyediakan angka 0 argumen kedua untuk operasi pembagian atau modulo.
FileNotFoundError: Exception ini muncul ketika berkas atau direktori yang program minta tidak ditemukan atau tidak ada.
Seperti nama-nama diatas, kebanyakan exception memiliki nama-nama yang cukup jelas.

Menangani Exception
Kode di awal artikel meminta pengguna untuk memasukkan integer sebagai sebuah input. Jika penggunanya tidak menyediakan masukkan integer, program-nya akan menghentikan eksekusi dan memunculkan nilai error exception-nya. Pada bagian ini, kita akan menulis beberapa kode untuk memberi tahu pengguna bahwa masukkan mereka bukanlah nilai integer yang valid.

Langkah pertama dari prosesnya adalah memasukkan kode yang kamu anggap bisa menimbulkan exception di dalam klausa try. Langkah selanjutnya adalah menggunakan keyword except untuk menangani exception yang terjadi pada kode di atas. Kode yang dimodifikasi untuk masukkan penggunanya akan tampah seperti berikut:


keep_asking = True
 
while keep_asking:
    try:
        x = int(input("Please enter a number: "))
        print("Dividing 50 by", x,"will give you :", 50/x)
    except ValueError:
        print("The input was not an integer. Please try again...")
Apa yang terjadi di sini adalah program-nya mencoba untuk mengeksekusi kodenya di dalam klausa try. Jika tidak ada exception yang muncul, prgoramnya kan melewati klause except dan sisa kode-nya akan dieksekusi secara normal. Jika sebuah exception muncul, program-nya akan melewatkan sisa kode di dalam klausa try dan tipe dari exception-nya akan dicocokkan dengan nama exception setelah keyword except. Dalam kasus yang cocok, kode di dalam klausa except akan dieksekusi terlebih dahulu dan sisa setelah klausa try akan dieksekusi secara normal.

Ketika kamu memasukkan sebuah integer sebagai masukkannya, program-nya memberikanmu hasil akhir dari pembagian. Ketika nilai non-integral disediakan, program-nya akan mencetak sebuah pesan memintamu untuk mencoba dan memasukkan sebuah integer lagi. Ingat kali ini, programnya tidak akan keluar secara paksa saat kamu memasukkan nilai yang tidak valid.

Kamu bisa memiliki banyak klausa except untuk menangai aneka exceptions. Tolong diingat bahwa handler hanya akan menangani exception yang terjadi dan berkoreponsi dengan klausa try. Mereka tidak akan menangani exception apapun yang muncul di handler exception yang lainnya.

Kamu juga bisa menangani banyak exception menggunakan satu klausa except dengan melwatkan exception tersebut ke klausa sebagai sebuah tuple.


except (ZeroDivisionError, ValueError, TypeError):
    print("Something has gone wrong..")
    # code to deal with the exception
Pada akhirnya, kamu juga bisa meninggalkan nama dari exceptionnya setelah keyword except. Pada umumnya ini tidak direkomendasikan karena sekarang kode-nya akan mengejar semua exception dan menangani mereka dengan cara yang sama. Ini tidak optimal karena kamu akan menangani seuah TypeError exception dengan cara yang sama dengan saat kamu menangani sebuah ZeroDivisionError exception. Saat menangani exception, akan lebih baik untuk menjadi se-spesifik mungkin dan hanya menangkap apa yang bisa kamu tangani.

Satu penggunaan yang mungkin untuk menangkap semua exception adalah dengan mencetak semua exception error di layar seperti pada kode berikut:


import math
import sys
 
try:
    result = math.factorial(2.4)
except:
    print("Something Unexpected has happened.",sys.exc_info()[0])
else:
    print("The factorial is", result)

Advertisement
Menggunakan Klause Else
Kamu juga bisa menggunakan sebuah klausa else di dalam pernyataan try ... except. Klausa else diperuntukkan untuk mengandung kode yang perlu dieksekusi jika klause try tidak memunculkan exception apapun. Ini bisa jadi berguna untuk memastikan bahwa kamu tidak menambahkan kode apapun ke blok try yang memiliki exception yang tidak ingin kamu tangkap. Satu hal yang perlu disebut adalah bahwa jika kamu memutuskan untuk menggunakan sebuah klausa else, kamu harus memasukkan-nya setelah semua klausa except namun sebelum blok finally.

Pada kasus kita, kita bisa memindahkan baris yang mencetak hasilkan ke pembagian kita di dalam blok else.


keep_asking = True
 
while keep_asking:
    try:
        x = int(input("Please enter a number: "))
    except ValueError:
        print("The input was not a valid integer. Please try again...")
    else:
        print("Dividing 50 by", x,"will give you :", 50/x)
Membersihkan Menggunakan Klausa Finally
Mari katakan kamu harus menulis beberapa kode di dalam blok try yang diperuntukkan untuk melalukan sebuah tugas dengan menggunakan jumlah resource yang besar. Penting untuk melepas resource tersebut kembali ketika kamu selesai menggunakannya. Ini bisa diraih dengan mudah dengan menggunakan klause finally.

Kode di dalam klausa finally selalu dieksekusi terlepas dari baik blok try memunculkan exception maupun tidak.


keep_asking = True
 
while keep_asking:
    try:
        x = int(input("Please enter a number: "))
    except ValueError:
        print("The input was not a valid integer. Please try again...")
    else:
        print("Dividing 50 by", x,"will give you :", 50/x)
    finally:
        print("Already did everything necessary.")
Jika ada klausa except yang dispesifikasikan tidak menangani exception yang muncul, exception yang sama akan dimunculkan kembali setelah eksekusi kode di dalam blok finally.

Contoh yang Lebih Rumit
Pada bagian ini, kita akan menulis sebuah program untuk menangani aneka exceptions. Hanya seperti contoh-contoh sebelumnya, kita akan melakukan beberapa operasi matematis. Namun, kali ini kita akan mengambil beberapa input dari sebuah list.

Kode berikut mengecek dua exceptions, TypeError dan ValueError. Blok else diugnakan untuk mencetak faktorial-nya. Kamu bisa lihat di output-nya bahwa kode-nya hanya dieksekusi ketika tidak ada exception muncul.


import math
 
number_list = [10,-5,1.2,'apple']
 
for number in number_list:
    try:
        number_factorial = math.factorial(number)
    except TypeError:
        print("Factorial is not supported for given input type.")
    except ValueError:
        print("Factorial only accepts positive integer values.", number," is not a positive integer.")
    else:
        print("The factorial of",number,"is", number_factorial)
    finally:
        print("Release any resources in use.")
Kode di atas menghasilkan output berikut:

The factorial of 10 is 3628800
Releasing any resources in use.
 
Factorial only accepts positive integer values. -5  is not a positive integer.
Releasing any resources in use.
 
Factorial only accepts positive integer values. 1.2  is not a positive integer.
Releasing any resources in use.
 
Factorial is not supported for given input type.
Releasing any resources in use.
Hal lain yang penting untuk diperhatikan adalah bahwa kode di dalam klausa finally dieksekusi untuk tiap item dalam list.

Hal Terkahir
Saya harap panduan ini akan membantumu memahami penanganan exception di Python. Di samping itu, jangan ragu untuk melihat apa yang tersedia untuk dijual dan dipelajari di marketplace. Dan jangan ragu untuk menanyakan pertanyaan apapun dan menyediakan umpan balik yang berguna menggunakan umpan berikut.

Menangani exception dengan tepat bisa jadi sangat membantu pada situasi dimana kelaur dari sebuah program ketika menerima sebuah input yang tidak diperkirakan tidak dapat dilakukan. Jika kamu punya pertanyaan terkait penanganan exception di Python tolong beri komentar.