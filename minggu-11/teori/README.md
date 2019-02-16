Menjadi Developer Web dengan Python dan Flask Bagian I: Hello World
Ditulis oleh Lord Voldemort, dipublikasi pada 21 Dec 2017 dalam kategori Tutorial
Menjadi Developer Web dengan Python dan Flask Bagian I: Hello World - CodePolitan.com
Artikel ini merupakan terjemahan Chapter 1: Hello, World! dari seri The Flask Mega-Tutorial karya Miguel Grinberg yang akan dirilis secara gratis bab per bab sampai bulan Mei 2018. Dukung penulis aslinya dengan membeli buku/video tutorial lengkapnya di sini.

Daftar Isi:
Menjadi Developer Web dengan Python dan Flask: Hello World (Artikel ini)
Menjadi Developer Web dengan Python dan Flask: Template
Menjadi Developer Web dengan Python dan Flask: Menampilkan dan Memproses Form
Memasang Python
Jika pembaca belum memiliki Python, silahkan pasang terlebih dahulu. Jika sistem operasi yang digunakan tidak memiliki package Python, silahkan unduh berkas pemasangnya dari website resmi Python. Jika menggunakan Microsoft Windows dengan SWL atau Cygwin, ingat bahwa pembaca tidak akan menggunakan Python versi native untuk Windows melainkan versi Unix-friendly yang bisa didapat dari Ubuntu (jika menggunakan WSL) atau dari Cygwin.

Untuk memastikan Python sudah terpasang dengan baik, buka sebuah jendela terminal dan ketikkan python3, atau jika tidak berhasil, coba hanya mengetikkan python. Berikut pesan yang seharusnya muncul:

$ python3
Python 3.5.2 (default, Nov 17 2016, 17:05:23)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> _
Interpreter Python sekarang sedang menunggu perintah-perintah PYthon yang akan kita masukkan. Di bab-bab mendatang kita akan belajar bagaimana memanfaatkannya untuk melakukan hal-hal berguna. Tapi untuk sekarang, kita hanya melakukan konfirmasi bahwa Python sudah terpasang dengan benar. Untuk keluar dari interactive prompt ini ketikkan exit() dan tekan Enter. Di Linux dan Mac OS X kita juga dapat keluar menggunakan Ctrl-D. Di Windows, shortcut untuk keluar adalah Ctrl-Z diikuti tombol Enter.

Memasang Flask
Langkah berikutnya ialah untuk memasang Flask, tapi sebelum kita melakukannya penulis ini memberitahu pembaca tentang best practice saat memasang package Python.

Dalam bahasa pemrograman Python, package seperti Flask tersedia di repositori publik dimana semua orang dapat mengunduh dan memasangnya. Repositori package resmi Python bernama PyPI, yang juga kepanjangan dari Python Package Index. Memasang sebuah package dari PyPI sangat mudah karena Python memiliki sebuah tool bernama pip yang melakukan proses pemasnagnanya (di Python 2.7 pip terpasang secara terpisah dari Python).

Untuk memasang sebuah package gunakan perintah pip sebagai berikut:

$ pip install <package-name>
Menariknya, cara ini mungkin tidak akan berjalan sesuai keinginan. Jika interpreter Python kita terpasanga secara global untuk seluruh pengguna, kita mungkin memerlukan akses administrator untuk menjalankan perintah di atas. Akan tetapi meski pemasangan di atas berhasil tanpa masalah, maka setiap script Python di komputer kita memiliki akses ke package ini. Bayangkan sebuah situasi dimana kita telah menyelesaikan sebuah aplikasi web yang menggunakan Flask versi 0.11 kemudian Flask meirlis versi 0.12. Lalu kita ingin membuat aplikasi web baru dengan Flask versi 0.12 ini, akan tetapi jika kita mengganti versi 0.11 dengan versi 0.12 ada resiko yang membuat aplikasi sebelunnya tidak berjalan dengan seharusnya. Apakah pembaca dapat melihat masalah ini? Akan lebih baik jika kita memasang Flask 0.11 hanya untuk digunakan oleh aplikasi lama dan memasang Flask 0.12 hanya untuk aplikasi yang baru.

Untuk menyelesaikan permasalahan di atas dimana kita harus menggunakna beberapa versi dari sebuah package untuk beberapa aplikasi, Python menggunakna konsep virtual environments. Sebuah virtual environment merupakan salinan utuh sebuah interpreter Python. Saat kita memasang package di sebuah virtual environment, Python di sistem utama tidak akan terpengaruh. Virtual environment juga memiliki keuntungan dimana mereka dimiliki oleh user sehingga tidak memerlukan akun administrator.

Mari kita mulai dengan membuat sebuah direktori dimana project kita akan disimpan. Penulis akan menamainya microblog karena ini adalah nama aplikasinya:

$ mkdir microblog
$ cd microblog
Jika menggunakan Python 3, virtual environment sudah ada secara otomatis sehingga bisa langsung dibuat dengan perintah:

$ python3 -m venv venv
Dengan perintah ini, kita meminta Python untuk menjalankan package venv yang kemudian membuatkan kita sebuah virtual environment bernama venv. venv pertama di perintah tadi merupakan nama package-nya sedangkan venv yang kedua merupakan nama direktori untuk menyimpan salinan interpreter Python. Jika bingun silahkan ganti venv yang kedua dengan nama yang lain. Dengan demikian setiap kali kita melakukan cd ke project ini kita dapat melihat virtual environment yang baru kita buat.

Harap dicatat bahwa beberapa sistem operasi mungkin akan menggunakan python bukannya python3 untuk perintah di atas. Beberapa sistem operasi masih menggunakan python untuk rilis Python 2.x dan python3 untuk versi 3.x sementara sistem operasi lain ada yang menggunakan python untuk versi 3.x.

Setelah perintah tadi selesai dijalankan, kita akan memiliki direktori baru bernama venv tempat menyimpan file-file virtual enviroment kita.

Jika masih menggunanka versi Python yang dirilis sebelum 3.4, virtual environment belum menjadi package bawaan sehingga harus dipasang terlebih dahulu. Untuk versi Python-python tadi, pasang aplikasi pihak ketika bernama virtualenv sebelum membuat virtual environment yang baru. Setelah virtualenv terpasanga, kita dapat membuat sebuah virtual environment menggunanka perintah:

$ virtualenv venv
Metode manapun yang digunakan, sekarang kita seharusnya sudah memiliki virtual environment. Mari kita beri tahu sistem bahwa kita ingin menggunakannya. Untuk menggunakan virtual environment kita harus mengaktifkannya dengan perintah:

$ source venv/bin/activate
(venv) $ _
Perintah untuk Microsoft Windows agak berbeda:

$ venv\Scripts\activate
(venv) $ _
Saat mengaktifkan virtual environment, konfigurasi terminal session kita dimodifikasi sehingga interpreter Python yang disimpan didalam virtual environment akan dipanggil saat kita mengetik python. Selain itu, terminal prompt ($) juga dimodifikasi untuk menampilkan nama virtual environment yang diaktifkan. Perubahan pada terminal session ini hanya bersifat sementara dan hanya terjadi saat diaktifkan saja, setelah terminal ditutup sesi yang berubah akan menjadi sediakala. Jika menggunakan beberapa tab sekaligus, kita juga bisa mengaktifkan beberapa virtual environment secara bersamaan.

Sekarang setelah kita memiliki virtual environment, kita bisa menambahkan Flask ke dalamnya:

(venv) $ pip install flask
Untuk memastikan Flask sudah terpasang, masuk ke interpreter Pyton lalu import Flask seperti ini:

>>> import flask
>>> _
Jika tidak ada error yang ditampilkan berarti Flask sudah terpasang dan siap digunakan.

Aplikasi "Hello, World" dengan Flask
Jika pembaca membuka website Flask, pembaca akan disambut dengan sebuah contoh aplikasi yang hanya terdiri dari lima baris kode saja. Daripada mengulang contoh yang ada disana, penulis akan menunjukkan contoh lain yang akan memberikan pembaca struktur dasar untuk membuat aplikasi yang lebih besar.

Aplikasi ini akan ada didalam sebuah package. Menurut konsep pemrograman Python, sebuah sub-direktori yang didalamnya ada file init.py akan dianggap sebauh package dan bisa di impor. Saat mengimpor sebuah package file init.py akan dieksekusi sebagai simbol dari package tersebut ke dunia luar.

Mari kita buat sebuah package bernama app, direktori yang akan menyimpan file aplikasi kita. Pastikan sekarang sudah berada di direktori microblog dan jalankan perintah:

(venv) $ mkdir app
File init.py untuk package app harus memiliki kode berikut:

from flask import Flask

app = Flask(__name__)

from app import routes
Skrip di atas hanya membuat sebuah objek application sebagai sebuah instance dari kelas Flask yang diimpor dari package flask. Variabel __name__ yang diberikan kepada kelas Flask adalah variabel yagn sudah dibuatkan oleh Python yang isinya merupakan nama module dimana ia digunakan. Flask menggunakna lokasi module yang dikirimkan sebagai titik awal dimana ia harus memuat file-file yang diperlukan misalnya file template yang akan kita bahas di bab 2. Memberikan __name__ setiap kali membuat konfigurasi Flask biasanya akan menjadi langkah terbaik. Objek application ini selanjutnya mengimpor modul routes, yang saat ini belum ada.

Satu hal yang mungkin akan membingungkan di awal adalah ada dua entitas bernama app. Package app dan objek app yang ada di perintah from app import routes. Variabel app yang ada di perintah tersebut merupakan sebuah instance kelas Flask di dalam skrip init.py, sehingga membuatnya menjadi bagian dari package app. (Sederhananya, app yang pertama itu disebut package karena dia folder yang di dalamnya ada init.py sedangkan app yang kedua itu nama objek di dalam file init.py tadi).

Keanehan lainnya ialah modul routes di impor di bagian bawah file bukan di bagian atas dimana umumkan dilakukan. Impor yang ada di bawah merupakan solusi untuk circular import, sebuah permasalahan umum yang dimiliki oleh aplikasi Flask. Kita akan melihat bahwa modul routes perlu mengimpor variabel app yang didefinisikan di script ini, jadi menyimpan import di bawah akan menghindari error yang dihasilkan oleh reference yang sama dari dua file ini.

Jadi apa yang akan ada di dalam modul routes? Routes adalah kumpulan URL yang akan di implementasi oleh aplikasi. Dalam dunia FLask, handler yang route aplikasi ditulis sebagai fungsi Python yang disebut dengan view function. View function akan memetakan satu atau lebih URL sehingga Flask akan tahu apa yang harus ia lakukan setiap kali klien memanggil sebuah URL.

Berikut ini view function pertama kita yang harus ditulis di sebuah modul baru bernama app/routes.py:

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
View function ini sangat sederhana, ia hanya memberikan sebuah string sapaan. Dua baris aneh @app.route di atas adalah decorator, fitur unik Python. Sebuah decorator memodifikasi fungsi yang mengikutinya. Satu pola umum dengan decorator ialah untuk menggunakannya sebagai callback di event tertentu. Dalam kasus ini, @app.route akan membuat sebuah hubungan antara URL yang diberikan sebagai argumen dengan fungsi di bawahnya. Pada contoh di atas, ada dua decorator yang masing-masing terhubung dengan URL / dan /index dengan fungsi di bawahnya. Artinya setiap kali sebuah web browser mengakses salah satu dari dua URL ini, Flask akan membanggil fungsi di bawahnya dan mengirimkan nilai balikan (perintah return) yang sudah dibuat sebagai sebuah response. Mungkin sekarang masih belum jelas terlihat, namun nanti akan jelas saat aplikasi ini dijalankan.

Untuk menyelesaikan aplikasi ini, kita perlu memiliki skrip Python di direktori utama yang mendefinisikan instance Flask. Mari buat skrip bernama microblog.py dan tambah sebaris kode berikut:

from app import app
Masih ingat kan dua app sebelumnya? Di sini kita menggunakan kedua app di baris yang sama. instance aplikasi Flask yang bernama app merupakan bagian dari package app. Perintah from app import app akan mengimpor variabel app. Jika pembaca masih bingung, silahkan ubah salah satunya dengan nama yang berbeda.

Hanya untuk memastiakn bahwa semua yang kita lakukan sudah benar, lihat diagram dari struktur aplikasi yang sudah kita buat sejauh ini:

microblog/
  venv/
  app/
    __init__.py
    routes.py
  microblog.py
percaya atau tidak, aplikasi pertama kita sudah selsai! Sebelum menjalankannya, Flask perlu diberitahu bagaimana mengimpor aplikasi kita dengan mengatur environment variable FLASK_APP:

(venv) $ export FLASK_APP=microblog.py
Jika pembaca menggunakan Microsoft Windows, gunakan set untuk menggantikan export.

Apakah pembaca sudah siap? Untuk menjalankan aplikasi web pertama kita dengan Flask, jalankan perintah:

(venv) $ flask run
 * Serving Flask app "microblog"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Setelah server aktif ia akan menunggu koneksi dari klien. Pesan yang ditampilkan oleh flask run mengindikasikan bahwa server berjalan di IP address 127.0.0.1, alamat dari komputer kita sendiri. Alamat ini juga sangat umum dikenal dengan nama lain yaitu: localhost. Server ini meunggu di alamat port khusus biasanya di port 443 atau 80. Karena aplikasi ini berjalan di komputer sendiri (development environment), maka FLask bebas menggunakan port yang masih kosong 5000. Sekarang buka browser lalu buka URL berikut:

http://localhost:5000/
Atau bisa juga mengakses alamat:

http://localhost:5000/index
Mulai terlihat? URL yang pertama akan memanggil / sedangkan URL yang kedua akan memanggil /index. Kedua route ini terhubung dengan sebuah fungsi yang sama sehingga mereka akan menghasilkan output yang sama pula. Jika memasukkan URL yang lain pembaca akan mendapatkan error karena yang dikenal baru dua URL ini. Hello, World!