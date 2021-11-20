import requests, threading, time, urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from random import choice, SystemRandom, randint
from fake_headers import Headers
from stem import Signal
from stem.control import Controller

class Zombi(threading.Thread):

    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.os = None
        self.browser = None
        self.candidat = Candidat
        self.messages = []
        self.Proxies = {0: {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'},
                        1: {'http': 'socks5://127.0.0.1:9060', 'https': 'socks5://127.0.0.1:9060'},
                        2: {'http': 'socks5://127.0.0.1:9070', 'https': 'socks5://127.0.0.1:9070'},
                        3: {'http': 'socks5://127.0.0.1:9080', 'https': 'socks5://127.0.0.1:9080'},
                        4: {'http': 'socks5://127.0.0.1:9090', 'https': 'socks5://127.0.0.1:9090'},
                        5: {'http': 'socks5://127.0.0.1:9100', 'https': 'socks5://127.0.0.1:9100'},
                        6: {'http': 'socks5://127.0.0.1:9200', 'https': 'socks5://127.0.0.1:9200'},
                        7: {'http': 'socks5://127.0.0.1:9300', 'https': 'socks5://127.0.0.1:9300'},
                        8: {'http': 'socks5://127.0.0.1:9400', 'https': 'socks5://127.0.0.1:9400'},
                        }
        self.Ports_control = {0: 9051, 1: 9061, 2: 9071, 3: 9081, 4: 9091, 5: 9101, 6: 9201, 7: 9301, 8: 9401}

    def run(self):
        try:
            print('{}[+]{} {} Agent wakes up'.format(bcolors.OKCYAN, bcolors.GREEN, self.threadID))
            while True:
                try:
                    # Inicializimi
                    self.os = choice(list(Config.get('os'))) #os[1]  # choice(os)
                    self.browser = choice(list(Config.get('browser')))
                    self.messages = [
                        '{}[#]{} New Vote ---> Agent {}'.format(bcolors.OKCYAN, bcolors.GREEN, self.threadID)]

                    self.candidat = choice(Candidat)

                    human = simulate(self.os,self.browser,self.Proxies.get(self.threadID),self.messages,self.candidat)
                    human.init_session()

                    human._token()

                    human._index()

                    human._Accest_token()

                    human._index_poll()

                    human._upgrade_socket()

                    human._vote()

                    human.print_time()
                    human.renew_connection(Config.get('torauth'), self.Ports_control.get(self.threadID))

                except Exception as e:
                    print(f'{bcolors.FAIL}[*]{bcolors.WARNING} Ndodhi nje gabim! {bcolors.FAIL}{e}')

            print('{}[-]{} {} Agent going to sleep'.format(bcolors.FAIL, bcolors.WARNING, self.threadID))

        except KeyboardInterrupt as ex:
            print("{}[*]{} {} Agent fired...".format(bcolors.FAIL, bcolors.WARNING, self.threadID))
            exit()

class SmartZombie(Zombi):

    def run(self):
        try:
            print('{}[+]{} {} Agent wakes up'.format(bcolors.OKCYAN, bcolors.GREEN, self.threadID))
            while True:
                try:
                    # Inicializimi
                    self.os = choice(list(Config.get('os')))  # os[1]  # choice(os)
                    self.browser = choice(list(Config.get('browser')))
                    self.messages = ['{}[#]{} New Vote ---> Agent {}'.format(bcolors.OKCYAN, bcolors.GREEN, self.threadID)]
                    self.candidat = choice(Candidat)

                    human = simulate(self.os, self.browser, self.Proxies.get(self.threadID),self.messages,self.candidat)
                    human.init_session()
                    time.sleep(randint(0, 2))
                    human._token()
                    time.sleep(randint(0, 2))
                    human._index()
                    time.sleep(randint(0, 2))
                    human._Accest_token()
                    time.sleep(randint(0, 2))
                    human._index_poll()
                    time.sleep(randint(0, 2))
                    human._upgrade_socket()
                    time.sleep(randint(0, 2))
                    human._vote()
                    time.sleep(randint(0, 2))
                    human.print_time()
                    human.renew_connection(Config.get('torauth'), self.Ports_control.get(self.threadID))
                    time.sleep(randint(0, 2))
                except Exception as e:
                    print(f'{bcolors.FAIL}[*]{bcolors.WARNING} Ndodhi nje gabim! {bcolors.FAIL}{e}')

                # self.proxNr += 1
            print('{}[-]{} {} Agent going to sleep'.format(bcolors.FAIL, bcolors.WARNING, self.threadID))

        except KeyboardInterrupt as ex:
            print("{}[*]{} {} Agent fired...".format(bcolors.FAIL, bcolors.WARNING, self.threadID))
            exit()

class simulate:

    def __init__(self,os,browser,proxy,messages,candidat):
        self.os = os
        self.browser = browser
        self.useragent = None
        self.Proxy = proxy
        self.cookie = ''
        self.messages = messages
        self.cookie = None
        self.token = None
        self.useragent = None
        self.X_Access_Token = None
        self.X_Websocket_Url = None
        self.Sec_Websocket_Accept = None
        self.code = Poll_url.split('/')[4]
        self.candidat = candidat

    def init_session(self):

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # warning Disable

        self.useragent = Headers(browser=f'{self.browser}', os="win", headers=False).generate().get(
            'User-Agent')  # Generate User Agent

        headers = {
            'Host': 'www.riddle.com',
            'Sec-Ch-Ua': '";Not A Brand";v="99", "Chromium";v="94"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': f'"{self.os.capitalize()}"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': f'{self.useragent}',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        response = requests.get(Poll_url, headers=headers, verify=False,
                                proxies=self.Proxy)

        self.cookie = response.cookies  # Cookie
        self.messages.append('{}[#]{} Cookie {}'.format(bcolors.OKBLUE, bcolors.GREEN, self.cookie.values()[0]))

    def _token(self):

        headers = {
            'Host': 'www.riddle.com',
            'Sec-Ch-Ua': '";Not A Brand";v="99", "Chromium";v="94"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': f'"{self.os.capitalize()}"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': f'{self.useragent}',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Dest': 'iframe',
            'Referer': f'{Poll_url}',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        response = requests.get('https://www.riddle.com/a/{}'.format(self.code), headers=headers, cookies=self.cookie,
                                verify=False,
                                proxies=self.Proxy)

        self.token = str(response.content.decode()).split(';')[0].split('appToken = ')[1].replace("'", "")  # get Token
        self.messages.append('{}[#]{} Token: {}'.format(bcolors.OKBLUE, bcolors.GREEN, self.token))

    def _index(self):

        headers = {
            'Host': 'www.riddle.com',
            'Content-Length': '19',
            'Sec-Ch-Ua': '";Not A Brand";v="99", "Chromium";v="94"',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': f'{self.useragent}',
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, */*',
            'X-Requested-With': 'XMLHttpRequest',
            'Apptoken': f'{self.token}',
            'Sec-Ch-Ua-Platform': f'"{self.os.capitalize()}"',
            'Origin': 'https://www.riddle.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.riddle.com/a/{}'.format(self.code),
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '{"riddleId":' + f'{self.code}' + '}'
        requests.post('https://www.riddle.com/embed/stats/get', headers=headers, cookies=self.cookie, data=data,
                                 verify=False, proxies=self.Proxy)

    def _Accest_token(self):

        headers = {
            'Host': 'www.riddle.com',
            'Sec-Ch-Ua': '";Not A Brand";v="99", "Chromium";v="94"',
            'Accept': 'application/json, text/plain, */*',
            'X-Requested-With': 'XMLHttpRequest',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': f'{self.useragent}',
            'Apptoken': f'{self.token}',
            'Sec-Ch-Ua-Platform': f'"{self.os.capitalize()}"',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.riddle.com/a/{}'.format(self.code),
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        response = requests.get('https://www.riddle.com/ws/handshake/access-token/{}'.format(self.code), headers=headers,
                                cookies=self.cookie, verify=False, proxies=self.Proxy)

        self.X_Access_Token = response.headers.get('X-Access-Token')
        self.X_Websocket_Url = response.headers.get('X-Websocket-Url')

    def _index_poll(self):
        headers = {
            'Host': 'www.riddle.com',
            'Content-Length': '652',
            'Sec-Ch-Ua': '";Not A Brand";v="99", "Chromium";v="94"',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': f'{self.useragent}',
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, */*',
            'X-Requested-With': 'XMLHttpRequest',
            'Apptoken': f'{self.token}',
            'Sec-Ch-Ua-Platform': f'"{self.os.capitalize()}"',
            'Origin': 'https://www.riddle.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.riddle.com/a/{}'.format(self.code),
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '{"dataV1":[{"riddleId":' + f'{self.code}' + ',"data":"' + f'{self.code}' + '.start","event":"start","isFreetextAnswer":false},{"riddleId":' + f'{self.code}' + ',"data":"' + f'{self.code}' + '.' + f'{self.candidat}' + '","event":"answer","isFreetextAnswer":false},{"riddleId":' + f'{self.code}' + ',"data":"' + f'{self.code}' + '.finish","event":"finish","isFreetextAnswer":false}],"dataV2":"{\\"id\\":null,\\"messageType\\":1,\\"commandId\\":1,\\"scope\\":1,\\"fwd\\":[{\\"riddleId\\":' + f'{self.code}' + ',\\"messageType\\":1,\\"commandId\\":1,\\"category\\":\\"core_metrics\\",\\"label\\":\\"start\\"},{\\"riddleId\\":' + f'{self.code}' + ',\\"messageType\\":1,\\"commandId\\":1,\\"category\\":\\"answer\\",\\"label\\":\\"1.3\\"},{\\"riddleId\\":' + f'{self.code}' + ',\\"messageType\\":1,\\"commandId\\":1,\\"category\\":\\"core_metrics\\",\\"label\\":\\"finish\\"}]}"}'

        requests.post('https://www.riddle.com/embed/stats/enqueue', headers=headers, cookies=self.cookie,
                                 data=data, verify=False, proxies=self.Proxy)

    def _upgrade_socket(self):
        import string
        #socket_key1 = '93Jk5lASFUYPqLKZgaShPw==' # socket key is in base64
        # But more fast and less power usage method, is to generate random string in b64 style
        socket_key = ''.join(SystemRandom().choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for _ in
                             range(22)) + '=='

        headers = {
            'Host': 'www.riddle.com',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': f'{self.useragent}',
            'Upgrade': 'websocket',
            'Origin': 'https://www.riddle.com',
            'Sec-Websocket-Version': '13',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Sec-Websocket-Key': f'{socket_key}',
        }

        response = requests.get(f'https:{str(self.X_Websocket_Url).split(":")[1]}', headers=headers, cookies=self.cookie,
                                verify=False, proxies=self.Proxy)

        self.Sec_Websocket_Accept = response.headers.get('Sec-Websocket-Accept')
        self.messages.append(
            '{}[#]{} URL https:{}'.format(bcolors.OKBLUE, bcolors.GREEN, str(self.X_Websocket_Url).split(":")[1]))
        self.messages.append('{}[#]{} Sec Websocket Accept: {}  -- Status : {}'.format(bcolors.OKBLUE, bcolors.GREEN,
                                                                                       self.Sec_Websocket_Accept,
                                                                                       response.status_code))

    def _vote(self):
        headers = {
            'Host': 'www.riddle.com',
            'Content-Length': '446',
            'Sec-Ch-Ua': '";Not A Brand";v="99", "Chromium";v="94"',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': f'{self.useragent}',
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, */*',
            'X-Requested-With': 'XMLHttpRequest',
            'Apptoken': f'{self.token}',
            'Sec-Ch-Ua-Platform': f'"{self.os.capitalize()}"',
            'Origin': 'https://www.riddle.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.riddle.com/a/{}'.format(self.code),
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        data = '{"msg":"{\\"id\\":null,\\"messageType\\":1,\\"commandId\\":1,\\"scope\\":1,\\"fwd\\":[{\\"riddleId\\":' + f'{self.code}' + ',\\"messageType\\":1,\\"commandId\\":1,\\"category\\":\\"core_metrics\\",\\"label\\":\\"start\\"},{\\"riddleId\\":' + f'{self.code}' + ',\\"messageType\\":1,\\"commandId\\":1,\\"category\\":\\"answer\\",\\"label\\":\\"1.' + f'{self.candidat}' + '\\"},{\\"riddleId\\":' + f'{self.code}' + ',\\"messageType\\":1,\\"commandId\\":1,\\"category\\":\\"core_metrics\\",\\"label\\":\\"finish\\"}]}","accessToken":"' + f'{self.X_Access_Token}' + '"}'

        response = requests.post('https://www.riddle.com/ws/fallback', headers=headers, cookies=self.cookie, data=data,
                                 verify=False, proxies=self.Proxy,
                                 timeout=3)

        self.messages.append('{}[#]{} Response {}'.format(bcolors.OKBLUE, bcolors.GREEN, response.content.decode()))

    def renew_connection(self,torauth, Port):
        with Controller.from_port(port=Port) as controller:
            controller.authenticate(password=torauth)
            controller.signal(Signal.NEWNYM)

    def print_time(self):
        total = [(i + '\n') for i in self.messages] # new line
        '''for i in self.messages:
            total += str(i) + '\n'''
        print(total)

class bcolors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == "__main__":

    # Default Global
    # Proxies = [line.strip() for line in open('proxys-list.txt', 'r')] # alternative Proxy list
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # Disable Warning

    Config = {'Candidat':None,
              'Poll_url':None,
              'exitFlag':True,
              'Threadnr':9,
              'Version':1.3,
              'torauth':'tor-hash',
              'os':['win', 'linux', 'android', 'ios'],
              'browser':['chrome', 'firefox']} # generate Tor password for your port and change with 'tor-hash' update it in all /etc/torrc

    # Header and informations
    __header__ = '{}[!]{} Starting Program\n' \
               '\n{}[+]{} Version : {}\n' \
               '{}[+]{} Github  : {}\n' \
               '{}[*]{} Threads : {} - Default\n' \
               '\n{}[#]{} Credits : Adriatik Mehmeti - Author\n'.format(bcolors.OKCYAN,bcolors.WARNING,
                                                                        bcolors.OKCYAN,bcolors.OKBLUE,Config.get('Version'),
                                                                        bcolors.OKCYAN, bcolors.OKBLUE,'Linku',
                                                                        bcolors.OKCYAN,bcolors.OKBLUE,Config.get('Threadnr'),
                                                                        bcolors.OKCYAN,bcolors.GREEN)

    # Control Authorize
    while Config.get('exitFlag'):
        print(__header__)
        if input(f'{bcolors.OKCYAN}[?]{bcolors.WARNING} Do you AUTHORIZE the operation ? [Y]es or [N]o : ').lower() == 'y':
            Config['exitFlag'] = False
        else:
            print(f"\n{bcolors.OKCYAN}[X]{bcolors.FAIL} The operation was canceled!", "\n[X] Programm aborted.")
            exit()

    # Get Url
    while Config.get('Poll_url') == None:
        temp = input(f'{bcolors.WARNING}[?] Poll Link: ')
        if temp.count("https") == 0:
            pass
        else:
            Poll_url = temp
            temp = ''

    # Get option to vote
    while Config.get('Candidat') == None:
        temp = input(f'{bcolors.WARNING}Candidat <start from 0> : ')
        if temp != '':
            Candidat = str(temp).split(',') if temp.count(',') > 0 else str(temp)
            temp = ''

    # Start Zombies # For littel confusion replace Zombie with SmartZombie
    try:
        print(f'\n\n{bcolors.OKCYAN}[+]{bcolors.WARNING} Initializing.....\n\n')
        for i in range(Config.get('Threadnr')):
            Zombi(i).start()
            time.sleep(randint(0, 3)) # time needed to init conf

        print(f"\n\n{bcolors.OKCYAN}[#]{bcolors.WARNING} You have done your job!!!!\n\n")

    except KeyboardInterrupt as ex:
        print(f"{bcolors.OKCYAN}[#]{bcolors.FAIL} Programm aborted")
        exit()
