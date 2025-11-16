
#buat akun
def buat_akun(daftar_pengguna):
    username_baru = input('Masukkan username: ')
    password_baru = input('Masukkan password: ')
    daftar_pengguna[username_baru] = password_baru
    print('Akun berhasil dibuat!')
  
#login
def login(daftar_pengguna):
    username = input('Username: ')
    password = input('Password: ')
    if username in daftar_pengguna and daftar_pengguna[username] == password:
        print('Login berhasil!')
    else: 
        print('Login gagal. Username atau Password salah.')

#bikin menu
daftar_pengguna = {}
while True:
    print('Menu')
    print('1. Login')
    print('2. Buat Akun')
    print('3. Keluar')
    print(' ')
    pilihan = input('Pilih Menu: ')
    if pilihan == '1':
        login(daftar_pengguna)
    elif pilihan == '2':
        buat_akun(daftar_pengguna)
    elif pilihan == '3':
        break
    else:
        print('Pilihan tidak valid.')        
            

        