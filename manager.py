from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os, random
from colorama import init, Fore
from time import sleep

init()

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]

try:
    import requests
except ImportError:
    print(f'{lg}[i] Gerekli Modüller Yükleniyor...{n}')
    os.system('pip install requests')

def banner():
    import random
    # fancy logo
    b = [
    '     ____           _____                  ',              
    '    / __ )__  __   / ___/___  ____ ___     ', 
    '   / __  / / / /   \__ \/ _ \/ __ `__ \    ',
    '  / /_/ / /_/ /   ___/ /  __/ / / / / /    ',
    ' /_____/\__, /   /____/\___/_/ /_/ /_/     ',
    '       /____/                               '
    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    #print('=============SON OF GENISYS==============')
    print(f'   Version: 1.2 | Programlayan: By Sem{n}\n')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(lg+'[1] Yeni Hesap Ekleme'+n)
    print(lg+'[2] Yasaklanmış Hesapları temizleme'+n)
    print(lg+'[3] Hesap Silme'+n)
    print(lg+'[4] Güncelleme'+n)
    print(lg+'[5] Çıkış'+n)
    a = int(input('\nSeçiminizi Yapınız: '))
    if a == 1:
        new_accs = []
        with open('vars.txt', 'ab') as g:
            number_to_add = int(input(f'\n{lg} [~] Kaç adet telefon numarası ekleyeceksiniz?: {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{lg} [~] Telefon Numarasını Giriniz: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{lg} [i] Tüm hesaplar vars.txt dosyasına kaydedildi')
            clr()
            print(f'\n{lg} [*] Yeni Hesaplar günlük dosyasına işlendi\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                c.start(number)
                print(f'{lg}[+] Giriş Başarılı')
                c.disconnect()
            input(f'\n Menüye dönmek için ENTER tuşuna basınız...')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] Hesap bulunamadı! Lütfen bir hesap ekleyin ve tekrar deneyin')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] Enter the code: '))
                        print(f'{lg}[+] {phone} ban bulunamadı{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' Hesap banlandı!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'Tebrikler Banlı hesap bulunmamaktadır')
                input('\nMenüye dönmek için ENTER tuşuna basınız...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[i] Tüm banlanan hesaplar temizlendi'+n)
                input('\nMenüye dönmek için ENTER tuşuna basınız...')

    elif a == 3:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{lg}[i] Silinecek hesabın sıra numarasını seçiniz\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] Bir seçim yapınız: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('vars.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] Hesap Silindi{n}')
        input(f'\nMenüye dönmek için ENTER tuşuna basınız...')
        f.close()
    elif a == 4:
        # thanks to github.com/th3unkn0n for the snippet below
        print(f'\n{lg}[i] Güncelleme Kontrol Ediliyor...')
        try:
            # https://raw.githubusercontent.com/Cryptonian007/Astra/main/version.txt
            version = requests.get('https://raw.githubusercontent.com/Cryptonian007/Astra/main/version.txt')
        except:
            print(f'{r} İnternet bağlantısı bulunamadı')
            print(f'{r} Lütfen internete bağlanın ve tekrar deneyin')
            exit()
        if float(version.text) > 1.3:
            prompt = str(input(f'{lg}[~] Güncelleme Bulundu[Version {version.text}]. İndirilsin mi??[y/n]: {r}'))
            if prompt == 'y' or prompt == 'yes' or prompt == 'Y':
                print(f'{lg}[i] Güncelleme İndiriliyor...')
                if os.name == 'nt':
                    os.system('del add.py')
                    os.system('del manager.py')
                else:
                    os.system('rm add.py')
                    os.system('rm manager.py')
                #os.system('del scraper.py')
                os.system('curl -l -O https://raw.githubusercontent.com/Cryptonian007/Astra/main/add.py')
                os.system('curl -l -O https://raw.githubusercontent.com/Cryptonian007/Astra/main/manager.py')
                print(f'{lg}[*] Yeni sürüm güncellendi: {version.text}')
                input('Çıkmak için Enter tuşuna basınız...')
                exit()
            else:
                print(f'{lg}[!] Güncelleme Durduruldu.')
                input('Menüye dönmek için ENTER tuşuna basınız...')
        else:
            print(f'{lg}[i] Yazılım Zaten Güncel')
            input('Ana menüye gitmek için enter a basın...')
    elif a == 5:
        clr()
        banner()
        exit()
