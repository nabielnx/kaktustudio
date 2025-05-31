import os 
import time
import random
def clear_screen():
    os.system('cls')

welcome_message = 'WELCOME TO GAME ANJAY'
quit_message = 'Have a nice day!'

print(f'''
        ~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~{welcome_message}~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~
      ''')

answer = input('''
    Apakah kamu mau bermain?(Y/n)''')
if answer == 'Y' or answer == 'y':
    nickname = input('\nBuat nickname mu: ')
    age = int(input('berapa usiamu: '))
    minimum_age = 18
    if age >= minimum_age:
        clear_screen()
        print('Hello',nickname,',lets play the game')
        presiden = 'Prabowo Subianto'
        question1 = '''
     Question 1
     Siapa presiden ke 8 negara Indonesia?
     *Tulis nama dengan benar bung!!
     Answer:'''
        while True:
            answer = input(question1)
            clear_screen()
            if answer == presiden:
                print('\nHORE KAMU BENAR!!!!!')
                print('Oke lanjut question 2 dalam 2 detik.... ')
                time.sleep(2)
                clear_screen()
                odgj = 'orang dengan gangguan jiwa'
                question2 = '''
                Question 2
                Apa kepanjangan dari odgj? 
                Answer:'''
                while True:
                    answer2 = input(question2)
                    clear_screen()
                    if answer2 == odgj:
                        print(nickname, odgj)
                        print('yahahaha orang gila orang gila ')
                        lanjut = input('Ingin bermain game yang lain?(Y/n)')
                        if lanjut == 'Y' or lanjut == 'y':
                            game1 = 'tebak kartu'
                            kartu = '|_|'
                            kartu_benar = random.randint(1, 5)
                            kartu_kosong = [kartu] * 5
                            total_kartu = kartu_kosong.copy()
                            total_kartu[kartu_benar - 1] = '|@|'
                            attempts = 3
                            kartu_kosong = ' '.join(kartu_kosong)
                            game2 = 'scrambeld word'
                            print('1.',game1)
                            print('2.',game2)
                            pilihan = int(input('Chose the game(chose by number):' ))
                            while attempts > 0:
                                if pilihan == 1:
                                    print(kartu_kosong)
                                    pilihan_user = int(input('pilih 1 kartu yang menurutmu benar [1 / 2 / 3 / 4 / 5]:'))
                                    pilihan_user_confirm = input(f'Apakah kamu yakin kartu ke {pilihan_user}?(Y/n):')
                                    print('kamu memilih kartu ke',pilihan_user)
                                    if pilihan_user_confirm == 'n':
                                        print('yaudah')
                                        exit()
                                    elif pilihan_user_confirm == 'Y' or pilihan_user_confirm == 'y':
                                        if pilihan_user == kartu_benar:
                                            print('Yes pilihanmu benar bung')
                                            exit()
                                        else:
                                            attempts -= 1
                                            print(f'Wrong answer bung!!!,{attempts} sisa kesempatan')
                                            if attempts == 0:
                                                print(f'Game over!!, kartu yang benar berada pada nomor:{kartu_benar}')
                                                exit()
                                            elif lanjut == 'N' or lanjut == 'n':
                                                print('yaudah')
                                                exit()
                            else:
                                def scramble_word(word):
                                    return "".join(random.sample(word,len(word)))
                                words = ["tambah","kurang","kali","bagi"]
                                word = random.choice(words)
                                scrambled = scramble_word(word)
                                print('Scrambled word:', scrambled)
                                attempts = 3
                                while attempts > 0:
                                    guess = input('Guess the word:').lower()
                                    if guess == word:
                                        print('KAMU BENAR BUNG!!')
                                        exit()
                                    else:
                                        attempts -= 1
                                        print(f'SALAH BUNG {attempts}, sisa kesempatan')
                                        if attempts == 0:
                                            print(f'Game over! huruf yang benar adalah: {word}')
                                            exit()
                                        elif lanjut == 'N' or lanjut == 'n' : 
                                            print ('yaudah')
                                            exit()
                        else:
                            print('yaudah')
                            exit()
                    else:
                        print('\nKamu salah bung, cek kembali jawabanmu!!') 
            else:
                print('\nKamu salah bung, cek kembali jawaban mu!!')
    else:
        print('Hld on kids!, jika kamu baperan mending jangan main mwewewhehwe')
else:
    print('Yaudah,',quit_message)
    lanjut = input('Ingin bermain game yang lain?(Y/n)')
    if lanjut == 'Y' or lanjut == 'y':
        game1 = 'tebak kartu'
        kartu = '|_|'
        kartu_benar = random.randint(1, 5)
        kartu_kosong = [kartu] * 5
        total_kartu = kartu_kosong.copy()
        total_kartu[kartu_benar - 1] = '|@|'
        kartu_kosong = ' '.join(kartu_kosong)
        attempts = 3
        game2 = 'scrambeld word'
        print('1.',game1)
        print('2.',game2)
        pilihan = int(input('Chose the game(chose by number):' ))
        while attempts > 0:
            if pilihan == 1:
                print(kartu_kosong)
                pilihan_user = int(input('pilih 1 kartu yang menurutmu benar [1 / 2 / 3 / 4 / 5]:'))
                pilihan_user_confirm = input(f'Apakah kamu yakin kartu ke {pilihan_user}?(Y/n):')
                print('kamu memilih kartu ke',pilihan_user)
                if pilihan_user_confirm == 'n':
                    print('yaudah')
                    exit()
                elif pilihan_user_confirm == 'Y' or pilihan_user_confirm == 'y':
                    if pilihan_user == kartu_benar:
                        print('Yes pilihanmu benar bung')
                        exit()
                    else:
                        attempts -= 1
                        print(f'Wrong answer bung!!!, {attempts} sisa kesempatan')
                        if attempts == 0:
                            print(f'Game Over bung!!!, Posisi kartu benar adalah: {kartu_benar}')
                            exit()
        else:
            def scramble_word(word):
                return "".join(random.sample(word,len(word)))
            words = ["tambah","kurang","kali","bagi"]
            word = random.choice(words)
            scrambled = scramble_word(word)
            print('Scrambled word:', scrambled)
            attempts = 3
            while attempts > 0:
                guess = input('Guess the word:').lower()
                if guess == word:
                    print('KAMU BENAR BUNG!!')
                    break
                else:
                    attempts -= 1
                    print(f'SALAH BUNG {attempts} attempts left')
            if attempts == 0:
                print(f'Game over! huruf yang benar adalah{word}')
    elif lanjut == 'N' or lanjut == 'n' : 
        print ('yaudah')
        quit
            