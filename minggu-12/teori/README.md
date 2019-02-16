Pertanyaan Distribusi dan lingkungan Python untuk komputasi ilmiah


 
Saya mohon maaf dimuka jika pertanyaan ini terlalu luas. Saya berasal dari dunia MATLAB dan memiliki pengalaman yang relatif sedikit dengan Python.

Setelah menghabiskan beberapa waktu membaca tentang beberapa lingkungan berbasis Python dan distribusi untuk komputasi ilmiah, saya merasa bahwa saya masih tidak sepenuhnya memahami lanskap solusi atau hubungan yang tepat antara beberapa paket penting, termasuk:

SciPy 
Spyderlib 
Pythonxy
Mengenali Distribusi Python
Sage
Lebih spesifik:

Apakah ada paket di atas yang menyediakan fungsi serupa? Apakah mereka saling melengkapi?
Apakah pemasangan salah satu dari mereka termasuk atau memerlukan instalasi dari salah satu yang lain? Jika ya, yang mana termasuk atau yang mana?
Yang kurang penting, apakah ada paket lain yang serupa dengan yang di atas yang menyediakan fungsi serupa?

Terima kasih sebelumnya


 21  2017-07-16 18:20

asal

 

Jawaban:
Komputasi ilmiah dengan Python menggunakan bahasa vanila biasa dan menggerombol sekelompok modul, yang masing-masing menerapkan beberapa aspek fungsi MATLAB. Dengan demikian pengalaman dengan pemrograman ilmiah Python adalah sedikit kohesif c.f. MATLAB. Namun Python sebagai bahasa jauh lebih bersih. Begitu seterusnya.

Modul dasar yang diperlukan untuk komputasi ilmiah dengan Python adalah Numpy, Matplotlib, SciPy dan jika Anda melakukan perencanaan 3d, maka Mayavi/VTK. Semua modul ini bergantung pada Numpy.

Numpy Menerapkan tipe larik baru yang berperilaku mirip dengan larik MATLAB (yaitu penghitungan vektor cepat). Ini juga mendefinisikan beban fungsi untuk melakukan perhitungan ini yang biasanya dinamakan sama dengan fungsi serupa di MATLAB.

Matplotlib Memungkinkan untuk 2d merencanakan dengan perintah yang sangat mirip dengan MATLAB. Matplotlib juga mendefinisikan pylab, yang merupakan modul yang - dengan satu impor - membawa sebagian besar fungsi Numpy dan Matplotlib ke dalam namespace global. Ini berguna untuk skrip cepat / interaktif di mana Anda tidak ingin mengetik banyak awalan namespace.

SciPy adalah kumpulan modul Python yang diatur di bawah payung SciPy yang berguna bagi para ilmuwan. Rutinitas pas disediakan dalam modul SciPy. Numpy adalah bagian dari Scipy.

laba laba adalah IDE desktop (berdasarkan QT) yang secara longgar mencoba untuk meniru MATLAB IDE. Ini adalah bagian dari distribusi Python-XY.

IPython menyediakan shell Python interaktif yang disempurnakan yang berguna untuk mencoba kode dan menjalankan skrip Anda dan berinteraksi dengan hasilnya. Sekarang dapat disajikan ke antarmuka web serta konsol tradisional. Ini juga tertanam dalam IDE Spyder.

Distribusi
Mendapatkan semua modul ini berjalan di komputer Anda dapat memakan waktu dan sehingga ada beberapa distribusi yang mengemasnya (ditambah banyak modul lain) untuk Anda.

Python-XY, WinPython, Enthought dan baru-baru ini Anaconda semuanya merupakan distribusi paket lengkap yang mencakup semua modul inti, meskipun Enthought tidak dilengkapi dengan Spyder.

Sage adalah lingkungan pemrograman lain yang dilayani melalui web atau melalui baris perintah dan juga hadir sebagai paket lengkap termasuk banyak modul lainnya. Secara tradisional itu datang sebagai gambar VMWare berdasarkan pada instalasi Linux. Meskipun Anda menulis Python di lingkungan Sage, itu sedikit berbeda dengan pemrograman Python biasa, itu semacam mendefinisikan bahasa dan metodologi sendiri berdasarkan Python.

Jika Anda menggunakan Windows, saya akan menginstal WinPython. Ini menginstal semua yang Anda butuhkan termasuk Scipy dan Spyder (yang merupakan pengganti terbaik untuk MATLAB untuk Python IMHO) dan karena dirancang untuk berdiri sendiri tidak akan mengganggu instalasi Python lain yang mungkin Anda miliki pada sistem Anda. Jika Anda menggunakan OSX, Enthought mungkin adalah cara terbaik - Spyder dapat diinstal secara terpisah menggunakan misalnya. MacPorts. Untuk Linux Anda dapat menginstal komponen (Numpy, SciPy, Spyder, Matplotlib) secara terpisah.

Saya pribadi tidak suka cara Sage bekerja dengan Python 'tersembunyi di bawah tenda' tetapi Anda mungkin lebih suka itu.