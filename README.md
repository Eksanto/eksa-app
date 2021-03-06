Setelah menyelesaikan semua modul dan graded assignment pada Data Analytics Specialization di Algoritma Academy (https://algorit.ma/) maka peserta diberikan tugas akhir (Capstone Project). Pada tugas akhir ini setiap peserta harus mengimplementasikan proses analisis data yang telah dipelajari secara runtut dari awal hingga akhir (end-to-end). 

Terdapat 4 (empat) pilihan case yang tersedia, dan saya memilih salah satu proyek yaitu bertemakan 'Named Entity Recognition (NER) - API Service'. Proyek ini mengacu pada https://github.com/iqbalbasyar/ner-flask yaitu cara menggunakan modul NER di spaCy untuk mengidentifikasi orang, organisasi, atau lokasi dalam teks, lalu menerapkan API Python dengan Flask. 

Produk akhir penerapan spaCy dalam aplikasi NER API dapat diakses di https://eksa-api.herokuapp.com/. Server herokuapp akan berubah menjadi mode **'sleep'** karena idle beberapa saat, untuk mengaktifkannya cukup buka url **"eksa-api.herokuapp.com"** pada browser anda. NER yang diaplikasikan terbatas dalam bahasa Inggris, gunakan contoh teks berikut untuk mencoba pengenalan entitas.

Teks untuk dicoba:  
*"Apple is looking at buying U.K. startup for $1 billion. 
Mr. Maldonado flicked his turn signal and moved right and within seconds, his Ford Explorer pickup was hit by a Tesla that was traveling about 60 miles per hour on Autopilot. 
San Francisco considers banning sidewalk delivery robots. 
London is a big city in the United Kingdom."*

![spaCy](https://user-images.githubusercontent.com/40589863/125156635-ae417e00-e190-11eb-9d7d-c8df9e45befd.png)
image source : https://spacy.io/

Checkpoints : 
1. Instalasi : 1 poin
2. Membuat dan menggunakan model entity recognition : 2 poin
4. Membuat api untuk aplikasi entity recognition dengan tampilan web : 2 poin
5. Membuat api untuk aplikasi entity recognition tanpa tampilan web : 9 poin
6. Melakukan deployment aplikasi pada remote host : 2 poin
