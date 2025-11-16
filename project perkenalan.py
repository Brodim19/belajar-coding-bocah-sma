#Perkenalan

nama = input('Nama: ')  #perintah memasukan data
umur = int(input('Umur: ')) #sama saja tapi versi angka

print('Pilih tingkat pendidikan:')
print('1. SD')
print('2. SMP')
print('3. SMA')
pilihan = input('Masukkan nomor sesuai pendidikan Anda: ')
if pilihan == '1':
    pendidikan = 'SD'
elif pilihan == '2':
    pendidikan = 'SMP'
elif pilihan == '3':
    pendidikan = 'SMA'

kelas = input('kelas: ')

print(f'halo semua kenalin aku {nama},usia ku {umur}')  #untuk print semua data tadi
print(f'dan aku sekarang duduk di bangku {pendidikan} kelas {kelas}')
