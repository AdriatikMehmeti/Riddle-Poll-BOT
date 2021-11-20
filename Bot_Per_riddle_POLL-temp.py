import requests, threading, time, urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from random import choice ,SystemRandom
from fake_headers import Headers
from stem import Signal
from stem.control import Controller

# Default Global
torauth = 'sahdgkjlqhweuodlasjhqkuygfhqwuyger2837y4298751y3u4riyq87491941924yrt8yqhkjhgw2387yrew87yr324r7qyr36742t3841776238ryer'
os = ['win', 'linux', 'android', 'ios']
browser = ['chrome', 'firefox']
Proxies = [line.strip() for line in open('proxys-list.txt', 'r')]
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)      # Disable Warning

class Zombi (threading.Thread):

   def __init__(self, threadID):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.os = None
      self.browser = None
      self.cookie = None
      self.token = None
      self.useragent = None
      self.X_Access_Token = None
      self.X_Websocket_Url = None
      self.Sec_Websocket_Accept = None
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
      #self.Proxies = {}
      #self.proxNr = 0
      self.Ports_control = {0:9051,1:9061,2:9071,3:9081,4:9091,5:9101,6:9201,7:9301,8:9401}

   def run(self):
       try:
           print ('{}[+]{} {} Agent wakes up'.format(bcolors.OKCYAN,bcolors.GREEN,self.threadID))
           while True:
               try:
                   # Inicializimi
                   self.os = os[1]#choice(os)
                   self.browser = choice(browser)
                   self.messages = ['{}[#]{} New Vote ---> Agent {}'.format(bcolors.OKCYAN,bcolors.GREEN,self.threadID)]
                   self.code = Poll_url.split('/')[4]
                   self.candidat = choice(Candidat)
                   #self.Proxies = {0: {'http': f'socks5://{Proxies[self.proxNr]}', 'https': f'socks5://{Proxies[self.proxNr]}'}}#Proxies[self.proxNr]
                   init_session(self)
                   _token(self)
                   _index(self)
                   _Accest_token(self)
                   _index_poll(self)
                   _upgrade_socket(self)
                   _vote(self)
                   print_time(self.messages)
                   renew_connection(torauth, self.Ports_control.get(self.threadID))
                   time.sleep(1)
               except Exception as e:
                   print(f'{bcolors.FAIL}[*]{bcolors.WARNING} Ndodhi nje gabim! {bcolors.FAIL}{e}')

               #self.proxNr += 1
           print('{}[-]{} {} Agent going to sleep'.format(bcolors.FAIL,bcolors.WARNING,self.threadID))

       except KeyboardInterrupt as ex:
           print("{}[*]{} {} Agent fired...".format(bcolors.FAIL,bcolors.WARNING,self.threadID))
           exit()


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
                            proxies=self.Proxies.get(self.threadID))
    '''response = requests.get(Poll_url, headers=headers, verify=False,proxies=self.Proxies.get(0), timeout=2)'''
    self.cookie = response.cookies  # Cookie
    self.messages.append('{}[#]{} Cookie {}'.format(bcolors.OKBLUE,bcolors.GREEN,self.cookie.values()[0]))

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

    response = requests.get('https://www.riddle.com/a/{}'.format(self.code), headers=headers, cookies=self.cookie, verify=False,
                            proxies=self.Proxies.get(self.threadID))
    '''response = requests.get('https://www.riddle.com/a/{}'.format(self.code), headers=headers, cookies=self.cookie,verify=False,proxies=self.Proxies.get(0))'''
    self.token = str(response.content.decode()).split(';')[0].split('appToken = ')[1].replace("'", "")  # get Token
    self.messages.append('{}[#]{} Token: {}'.format(bcolors.OKBLUE,bcolors.GREEN,self.token))
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

    data = '{"riddleId":'+f'{self.code}'+'}'
    response = requests.post('https://www.riddle.com/embed/stats/get', headers=headers, cookies=self.cookie, data=data,
                             verify=False, proxies=self.Proxies.get(self.threadID))
    '''response = requests.post('https://www.riddle.com/embed/stats/get', headers=headers, cookies=self.cookie, data=data,
                             verify=False, proxies=self.Proxies.get(0))'''

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
                            cookies=self.cookie, verify=False, proxies=self.Proxies.get(self.threadID))
    '''response = requests.get('https://www.riddle.com/ws/handshake/access-token/{}'.format(self.code), headers=headers,
                            cookies=self.cookie, verify=False, proxies=self.Proxies.get(0))'''
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

    data = '{"dataV1":[{"riddleId":'+f'{self.code}'+',"data":"'+f'{self.code}'+'.start","event":"start","isFreetextAnswer":false},{"riddleId":'+f'{self.code}'+',"data":"'+f'{self.code}'+'.'+f'{self.candidat}'+'","event":"answer","isFreetextAnswer":false},{"riddleId":'+f'{self.code}'+',"data":"'+f'{self.code}'+'.finish","event":"finish","isFreetextAnswer":false}],"dataV2":"{\\"id\\":null,\\"messageType\\":1,\\"commandId\\":1,\\"scope\\":1,\\"fwd\\":[{\\"riddleId\\":'+f'{self.code}'+',\\"messageType\\":1,\\"commandId\\":1,\\"category\\":\\"core_metrics\\",\\"label\\":\\"start\\"},{\\"riddleId\\":'+f'{self.code}'+',\\"messageType\\":1,\\"commandId\\":1,\\"category\\":\\"answer\\",\\"label\\":\\"1.3\\"},{\\"riddleId\\":'+f'{self.code}'+',\\"messageType\\":1,\\"commandId\\":1,\\"category\\":\\"core_metrics\\",\\"label\\":\\"finish\\"}]}"}'

    response = requests.post('https://www.riddle.com/embed/stats/enqueue', headers=headers, cookies=self.cookie,
                             data=data, verify=False, proxies=self.Proxies.get(self.threadID))
    '''response = requests.post('https://www.riddle.com/embed/stats/enqueue', headers=headers, cookies=self.cookie,
                             data=data, verify=False, proxies=self.Proxies.get(0))'''

def _upgrade_socket(self):
    import string

    socket_key1 = '93Jk5lASFUYPqLKZgaShPw=='
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
                            verify=False, proxies=self.Proxies.get(self.threadID))
    '''response = requests.get(f'https:{str(self.X_Websocket_Url).split(":")[1]}', headers=headers, cookies=self.cookie,verify=False, proxies=self.Proxies.get(0))'''
    self.Sec_Websocket_Accept = response.headers.get('Sec-Websocket-Accept')
    self.messages.append('{}[#]{} URL https:{}'.format(bcolors.OKBLUE,bcolors.GREEN,str(self.X_Websocket_Url).split(":")[1]))
    self.messages.append('{}[#]{} Sec Websocket Accept: {}  -- Status : {}'.format(bcolors.OKBLUE,bcolors.GREEN,self.Sec_Websocket_Accept,response.status_code))

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
    data = '{"msg":"{\\"id\\":null,\\"messageType\\":1,\\"commandId\\":1,\\"scope\\":1,\\"fwd\\":[{\\"riddleId\\":'+f'{self.code}'+',\\"messageType\\":1,\\"commandId\\":1,\\"category\\":\\"core_metrics\\",\\"label\\":\\"start\\"},{\\"riddleId\\":'+f'{self.code}'+',\\"messageType\\":1,\\"commandId\\":1,\\"category\\":\\"answer\\",\\"label\\":\\"1.'+f'{self.candidat}'+'\\"},{\\"riddleId\\":'+f'{self.code}'+',\\"messageType\\":1,\\"commandId\\":1,\\"category\\":\\"core_metrics\\",\\"label\\":\\"finish\\"}]}","accessToken":"' + f'{self.X_Access_Token}' + '"}'

    response = requests.post('https://www.riddle.com/ws/fallback', headers=headers, cookies=self.cookie, data=data,
                             verify=False, proxies=self.Proxies.get(self.threadID),timeout=3) # Notic - Nuk ka pas proxy
    '''response = requests.post('https://www.riddle.com/ws/fallback', headers=headers, cookies=self.cookie, data=data,
                             verify=False, proxies=self.Proxies.get(0),timeout=3)  # Notic - Nuk ka pas proxy'''

    self.messages.append('{}[#]{} Response {}'.format(bcolors.OKBLUE,bcolors.GREEN,response.content.decode()))


def renew_connection(torauth,Port):
    with Controller.from_port(port=Port) as controller:
        controller.authenticate(password=torauth)
        controller.signal(Signal.NEWNYM)

def print_time(messages):
    #print("[+] [%s] Name: %s | koha: %s" % (Thread,name, time.ctime(time.time())),"\n[+] [%s] Email: %s | votoi: - [ %s ]" % (Thread,email, vota))
    total = ''
    for i in messages:
        total+=str(i)+'\n'
        #print(1)
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
    RowNr = None
    Candidat = None
    Poll_url = None
    exitFlag = True
    Threadnr = 9 #5

    # Header and informations
    print(f'{bcolors.OKCYAN}[!]{bcolors.WARNING} Starting Program','\n',
          f'\n{bcolors.OKCYAN}[+]{bcolors.OKBLUE} Checking resource...','\n',
          f'\n{bcolors.OKCYAN}[*]{bcolors.OKBLUE} Threads : {Threadnr} - Numbers of Agents (Human simultan)',
          f'\n{bcolors.OKCYAN}[#]{bcolors.GREEN} Credits : Adriatik Mehmeti - Author','\n',)

    # Control Authorize
    while exitFlag:
        if input(f'{bcolors.OKCYAN}[!]{bcolors.WARNING} Do you AUTHORIZE the operation ? [Y]es or [N]o : ').lower() == 'y':
            exitFlag = False
        else:
            print(f"\n{bcolors.OKCYAN}[X]{bcolors.FAIL} The operation was canceled!","\n[X] Programm aborted.")
            exit()

    while Poll_url == None:
        temp = input(f'{bcolors.WARNING}Poll Link: ')
        if temp.count("https") == 0:
            pass
        else:
            Poll_url = temp
            temp = ''

    while Candidat == None:
        temp = input(f'{bcolors.WARNING}Candidat <start from 0> : ')
        if len(temp) >= 0:
            Candidat = str(temp).split(',')
            temp = ''
        else:
            pass

    print(f'\n\n{bcolors.OKCYAN}[+]{bcolors.WARNING} Initializing.....\n\n')

    # Start Zombies
    try:
        for i in range(Threadnr):
            Zombi(i).start()
            time.sleep(2)

        print (f"\n\n{bcolors.OKCYAN}[#]{bcolors.WARNING} You have done your job!!!!\n\n")

    except KeyboardInterrupt as ex:
        print(f"{bcolors.OKCYAN}[#]{bcolors.FAIL} Programm aborted")
        exit()