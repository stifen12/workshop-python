Memulai Pemrograman Python di Windows
13 Replies
Semester lalu saya berkenalan dengan bahasa Python. Sintaksnya sendiri sudah tidak terlalu asing karena saya pernah menggunakannya di RenPy. Yang belum saya ketahui waktu itu adalah apa yang saya butuhkan untuk mulai mengembangkan program Python, terutama pada sistem operasi Windows 7.

Ada banyak situs berbahasa asing yang memberikan informasi mengenai pemrograman Python di Windows. Namun di sini saya ingin merangkum informasi tersebut berdasarkan pengalaman saya menggunakan Python selama 5 bulan terakhir. Hal-hal yang dibahas mencakup instalasi Python, IDE yang digunakan, menjalankan program, instalasi modul, dan troubleshooting.


1.0 | Instalasi Python
Download Python di http://www.python.org/download/ jika Python belum terinstall di komputer Anda. Sama seperti Java, secara default Python belum terinstall dalam sistem operasi Windows.

Ada Python2 dan Python3, yang mana yang harus saya unduh?

Penjelasan lebih detail dapat dibaca pada artikel Python2 or Python3. Pada intinya versi yang diunduh tergantung dengan kebutuhan Anda. Python 3 adalah yang terbaru dan yang direkomendasikan. Namun Python 2 masih sering digunakan karena beberapa library belum mendukung Python 3 dan kebanyakan distribusi Linux dan Mac masih menggunakan Python 2 sebagai defaultnya.
Yang saya gunakan di artikel ini adalah Python 3.3. File python.exe akan tersimpan di folder C:\PythonXX, dimana XX menandakan versi python yang terinstall cth: Python33 / Python27

Cukup jalankan installer dan Python akan terinstall secara otomatis. Untuk mengecek apakah Python telah berjalan, buka python.exe atau IDLE dan ketikkan print “Hello World” atau print(“Hello World”) jika Anda menggunakan Python 3.



2.0 | Python IDE
Anda hanya butuh text editor (Notepad, Notepad++) untuk mulai menulis script Python. Simpan file yang Anda buat dengan ekstensi .py dan script Anda siap untuk dijalankan. Tapi kalau Anda lebih suka bekerja menggunakan IDE, ada banyak Python IDE yang bisa digunakan di Windows.

2.1 IDLE
IDE bawaan Python. Dirancang sebagai IDE yang portabel dan sederhana untuk memudahkan programmer pemula. Namun karena keterbatasan fitur, IDLE tidak direkomendasikan bagi yang ingin mengembangkan program Python secara serius.

2.2 PyDev
Yang paling sering saya gunakan. PyDev adalah plugin Eclipse yang mendukung bahasa Python. PyDev mampu mendukung pengembangan program dari skala kecil hingga skala besar. Instalasi yang relatif rumit dibanding IDE lainnya mungkin jadi salah satu kelemahan PyDev.

Untuk menggunakan PyDev, pertama cek apakah Java Runtime Environment (JRE) sudah terinstall. Kalau belum Anda bisa mengunduhnya di http://www.java.com/. Setelah itu unduh Eclipse di http://www.eclipse.org/. Kalau Anda tidak tahu versi mana yang harus diunduh, saya sarankan memilih Eclipse IDE for Java Developers. Tidak ada installer untuk Eclipse, cukup unzip file yang telah diunduh ke lokasi yang Anda inginkan semisal C:\Program Files\Eclipse\

Untuk menginstall PyDev, buka Eclipse dan ikuti langkah berikut:

Pilih Help > Install New Software
Ketikkan http://pydev.org/updates pada field Work with:
Dua pilihan akan muncul. Pilih PyDev / PyDev For Eclipse. Jangan pilih PyDev Mylyn Integration.
Kalau Anda tidak ingin Eclipse mengontak situs lain selain PyDev, hapus tanda centang pada Contact all update sites– Ini akan mempercepat proses pengunduhan. Tapi kalau PyDev malah gagal terinstall, centang kembali pilihan tersebut.
Ikuti langkah selanjutnya dan setujui license-nya.
Pada saat instalasi, sebuah dialog yang bertuliskan Aptana Pydev mungkin akan muncul. Centang Aptana Pydev; PyDev; Aptana > OK
Setelah instalasi selesai, restart Eclipse.
Konfigurasi PyDev:

Pilih Window > Preferences > Pydev > Interpreter – Python
Pilih New…
Pada field Interpreter Name, masukkan nama yang Anda suka (cth: Python33). Pada field Interpreter Executable, browse direktori tempat python.exe berada (cth: C:\Python33\python.exe) lalu pilih OK
Pada jendela Selection Needed, pilih OK. Terus pilih OK hingga selesai. PyDev Anda siap untuk digunakan.
Untuk langkah-langkah yang disertai gambar, Anda bisa membuka halaman ini. Halaman tersebut juga menjelaskan langkah-langkah menulis dan menjalankan program Python di PyDev.

2.3 PyScripter & NINJA-IDE
Sejauh ini saya baru menggunakan Notepad++ / PyDev untuk menulis script Python. Tapi saya tertarik untuk mencoba 2 IDE yang saya sebutkan di atas. Semua IDE yang saya sebutkan di sini sifatnya gratis dan ada juga yang open source (PyScripter, NINJA-IDE). Anda bisa membuka halaman ini untuk daftar IDE yang lebih lengkap. Beberapa IDE pada daftar tersebut bersifat komersial.

3.0 | Menulis / Menjalankan Program Python
Setelah instalasi Python telah dilakukan dan anda sudah menentukan IDE apa yang akan digunakan, sekarang saatnya mencoba menulis program sederhana dan menjalankannya (buat saja sebuah program Hello World).

3.1 Menjalankan Program Python di Command Prompt
Jika Anda menulis script Python dengan text editor dan menyimpannya dengan ekstensi .py, Anda bisa menjalankannya lewat Command Prompt dengan perintah:

[lokasi python.exe] [lokasi script python yang dijalankan]

Contoh:
C:\Python33\python.exe c:\Users\nastarhitam\Desktop\hello.py
atau
python c:\Users\nastarhitam\Desktop\hello.py
Contoh ke 2 bisa dilakukan dengan terlebih dahulu memberitahu Windows lokasi python.exe berada. Pada desktop, pilih Start > Computer > System properties > Advanced system settings > Environment Variables. Pada daftar System variables, klik 2x pada variabel Path. Edit nilai Variable value dengan menambahkan lokasi python.exe (lihat contoh dibawah) lalu klik OK.

#Tambahkan lokasi folder python.exe di paling belakang. 

%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;c:\Program Files\Microsoft SQL Server\100\DTS\Binn\;c:\Python33\;
editvariable
3.2 Menjalankan Program Python IDLE
Jika Anda memilih untuk menggunakan IDLE (bawaan Python) sebagai IDE anda, maka anda bisa ikuti petunjuk berikut. Pada IDLE, pilih File > New Window. Tulis script Python di jendela yang baru terbuka. Setelah selesai, simpan file Anda dan jalankan dengan memilih Run > Run module (atau tekan F5) di jendela tempat Anda menulis script. Hasil output akan muncul di jendela utama IDLE.

3.3 Menjalankan Program Python di PyDev
Jika Anda memilih untuk menggunakan PyDev sebagai IDE anda, maka anda bisa ikuti petunjuk berikut. Buka Windows > Open Perspective > Other lalu pilih PyDev. Perspective didesain agar tools yang kita butuhkan dalam pekerjaan kita (misalnya menulis kode Python) dapat diakses dengan mudah. Saat dijalankan, Eclipse akan mengingat Perspective terakhir yang Anda gunakan.

Untuk membuat proyek baru:

pilih File > New > PyDev Project
Masukkan nama proyek, pilih “Python”, dan versi Python Anda. Centang Create default ‘src’ folder– Klik Finish.
Setelah selesai, klik kanan pada proyek yang baru Anda buat (di Package Explorer) lalu pilih New > PyDev Module
Isikan nama file. Biarkan field Package kosong. Klik Finish
File yang baru dibuat akan terbuka di Editor View dan siap untuk diedit.
Untuk menjalankannya, klik kanan file yang ingin dijalankan (pada Package Explorer) lalu pilih Run As > Python Run. Atau bisa juga dengan klik sekali pada file lalu tekan Ctrl + F11. Hasil output akan ditampilkan pada jendela Console View.

Untuk penjelasan dengan gambar, Anda bisa kembali merujuk ke halaman ini di bagian Writing Yout First Python Program.

4.0 | Instalasi Modul Python
Seringkali Anda akan membutuhkan modul / library / package yang terdapat di Internet. Beberapa library tersedia dalam format .exe yang bisa langsung dijalankan di Windows, tapi sayangnya lebih banyak yang tidak. Salah satu cara mudah untuk menginstall library Python di Windows adalah dengan menggunakan EasyInstall.

Download setuptools di sini (EasyInstall sepaket dengan setuptools). Setelah diinstall, saya sarankan Anda memberitahu Windows dimana lokasi EasyInstall berada dengan cara yang sama dengan sebelumnya. Punya saya ada di C:\Python33\Scripts\

#Tambahkan lokasi folder easy_install.exe di paling belakang

%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;c:\Program Files\Microsoft SQL Server\100\DTS\Binn\;c:\Python33\;c:\Python33\Scripts\;
Jalankan EasyInstall lewat Command Prompt. Misalkan Anda ingin menginstall modul numpy, maka perintahnya adalah:

#Jika Anda telah memberitahu Windows lokasi easy_install.exe
easy_install numpy

#Jika belum... (XX = versi Python Anda. cth: Python33)
C:\PythonXX\Scripts\easy_install.exe numpy
Jika Anda terhubung ke internet, EasyInstall secara otomatis akan mencari modul tersebut dan menginstallnya ke komputer Anda. Dokumentasi lengkap mengenai penggunaan EasyInstall dapat dibaca di EasyInstall doc. Dua perintah lain yang sering saya gunakan di EasyInstall adalah:

#Jika Anda ingin menginstall library dari situs tertentu
easy_install [alamat situs]

#Jika Anda telah mendownload file library-nya (.tar.gz/.zip/.egg)
easy_install [path file]
Untuk mengecek apakah library sudah terinstall, jalankan python.exe atau IDLE. Ketikkan:

import [nama library/modul]
Jika tidak ada pesan error yang muncul, berarti library sudah terinstall dengan benar dan siap untuk digunakan.

tesimport

Dengan informasi ini saya kira Anda sudah siap untuk mulai mengembangkan program Python di Windows. Mungkin metode yang ditawarkan di sini bukan yang terbaik atau terefisien, tapi setidaknya bisa dijadikan referensi bagi Anda. Dokumentasi pada http://python.org/ dapat dijadikan sumber referensi utama yang jauh lebih detail dan akurat.

Saat menulis artikel ini, saya menggunakan Python 3.3, Notepad++ 6.3.1, Eclipse Juno, dan Windows 7. Ke depannya saya berencana untuk terus memperbarui tulisan ini agar tetap konsisten dengan teknologi yang ada.

5.0 | Troubleshooting
5.1 Bisakah saya menginstall lebih dari 1 versi Python di komputer yang sama?
Bisa. Setiap versi Python akan terinstall di direktori yang berbeda. Pada komputer saya, Python 2.7 terinstall di C:\Python27 dan Python 3.3 terinstall di C:\Python33. Kedua Python ini dapat dianggap sebagai dua program yang berbeda. Library yang diinstall di salah satu versi Python tidak akan ikut terinstall di versi Python lainnya. Pada konfigurasi interpreter PyDev, Anda dapat menambahkan lebih dari satu versi Python interpreter. Pada daftar interpreter, versi yang letaknya paling atas yang akan digunakan untuk menginterpret script Python.

5.2 Code completition di PyDev selalu mengakibatkan PyDev crash/not responding.

Jika code completition (Ctrl + Spasi) mengakibatkan PyDev/Eclipse crash, bisa jadi ini kesalahan dari Eclipse sendiri. Tapi kalau ini hanya terjadi saat Anda menulis program Python, bisa jadi ini disebabkan python.exe diblokir oleh program firewall Anda. Solusinya sederhana, unblock python.exe dari firewall.

5.3 Program Python saya error ketika dijalankan di IDLE, tapi berhasil ketika dijalankan di Command Prompt.

Meski jarang, saya pernah menemui kendala semacam ini. Program yang bersangkutan membutuhkan koneksi ke internet. Ada kemungkinan ini disebabkan oleh firewall. Kalau ini pernah terjadi pada Anda, saya sarankan untuk menjalankan program lewat Command Prompt atau IDE yang Anda miliki.