''' UTS
1. Buat variabel jenis list berikut.
    
    Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu hasil studi mahasiswa',
            'Nama Lengkap',
            'NIM',
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil',
            'aktif',
            'Tanggal-Bulan-Tahun Lahir']
#(NOTED: sesuaikan dengan data anda)


2. Buat variabel nested list berikut.

MK =   [['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [3,2,3,2,3,3,3,2],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.50,3.00,3.75,4.00,3.75,3.50,3.75,3.00]]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, dan Nilai)

3. Buat Kode dengan hasil runing seperti berikut.


            INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                           JURUSAN SAINS
                    KARTU HASIL STUDI MAHASISWA
                          GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : NIM
Program/Prodi   : S1/Sistem Informasi A
Tahun Masuk     : 2023-Ganjil
Status          : Aktif
|--|--   12   --|--             31            --|-- 7 --|--    13   --|
-----------------------------------------------------------------------
No. Kode        |           Mata Kuliah         |  SKS  | Nilai (0-4) |
-----------------------------------------------------------------------
1   22A1209     | Matkul1                       |   3   |         3.50|
2   22A1210     | Matkul2                       |   2   |         3.00|
3   22A1211     | Matkul3                       |   3   |         3.75|
4   22A1212     | Matkul4                       |   2   |         4.00|
5   22A1213     | Matkul5                       |   3   |         3.75|
6   22A1214     | Matkul6                       |   3   |         3.50|
7   22A1215     | Matkul7                       |   3   |         3.75|
8   22A1216     | Matkul8                       |   2   |         3.00|
-----------------------------------------------------------------------
                                       TOTAL SKS:   21
-----------------------------------------------------------------------
|---------------------------------71-----------------------------------|
Summary:
Jumlah Mata Kuliah : 8 Mata Kuliah
Nilai Tertinggi    : 4.00  (22A1212 - Matkul4)
Nilai Terendah     : 3.00  (22A1211 - Matkul2)
IP Kumulatif       : 3.00
                                   
                                               Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------ 
'''



# Tulis Kode Jawaban di bawah!
#Buat variabel jenis list berikut.
Bio = ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu hasil studi mahasiswa',
            'Indra Wahyulla',
            '231031017',
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil',
            'aktif',
            '12-08-2005']

#Buat variabel nested list berikut.
MK =   [['Program Dasar','Kalkulus Dasar 1','Sains Terpadu','Bahasa Indonesia','Pengantar Teknoligi Informasi','Cinta Imtak Dan Iptek','Pancasila','Agama Islam'],
        [3,3,2,3,2,3,2,2],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.75,3.50,3.90,4.00,3.50,3.70,3.85,3.25]]

#Buat Kode dengan hasil runing seperti berikut.

print(Bio[0].center(100).upper())
print(Bio[2].center(100).upper())
print(Bio[3].center(100).upper())
print(Bio[9].center(100).upper(),Bio[8])
print()
print()
                    
print(f'Nama Lengkap    : {Bio[4].upper()}')
print(f'NIM             : {Bio[5].upper()}')
print(f'Program/Prodi   : {Bio[6].upper()}/{Bio[7].upper()}')
print(f'Tahun Masuk     : {Bio[8][:4]}-{Bio[9].title()}')
print(f'Status          : {Bio[-2].title()}')
print(f'''
-----------------------------------------------------------------------
No. Kode        |           Mata Kuliah         |  SKS  | Nilai (0-4) |
-----------------------------------------------------------------------
1   {MK[2][0]}     | {MK[0][0]}                 | {MK[1][0]}     |         {MK[3][0]}|
2   {MK[2][1]}     | {MK[0][1]}              | {MK[1][1]}     |          {MK[3][1]}|
3   {MK[2][2]}     | {MK[0][2]}                 | {MK[1][2]}     |          {MK[3][2]}|
4   {MK[2][3]}     | {MK[0][3]}              | {MK[1][3]}     |          {MK[3][3]}|
5   {MK[2][4]}     | {MK[0][4]} | {MK[1][4]}     |          {MK[3][4]}|
6   {MK[2][5]}     | {MK[0][5]}         | {MK[1][5]}     |          {MK[3][5]}|
7   {MK[2][6]}     | {MK[0][6]}                     | {MK[1][6]}     |         {MK[3][6]}|
8   {MK[2][7]}     | {MK[0][7]}                   | {MK[1][7]}     |         {MK[3][7]}|
-----------------------------------------------------------------------
                                       TOTAL SKS:   20
-----------------------------------------------------------------------
Summary:
Jumlah Mata Kuliah : 8
Nilai Tertinggi    : 4.00  (22A1212 - Bahasa Indonesia)
Nilai Terendah     : 3.25  (22A1216 - Agama Islam)
IP Kumulatif       : 3.00
                                   
                                               Parepare, 25 Oktober 2023



                                                     {Bio[4].upper()}     
                                                     ---------------''')