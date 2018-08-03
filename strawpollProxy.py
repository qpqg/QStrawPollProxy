import requests
import os
from re import findall
#check20369851
def banner():
    os.system("clear")
    __author__ = "Qiuby Zhukhi"
    __TEAM__ = "-- [ PBM-TEAM ] --"
    print """                                        

     _         _        
    / \  _   _| |_ ___  Author: {}
   / _ \| | | | __/ _ \ Team: {}
  / ___ \ |_| | || (_) |StrawPoll.com
 /_/   \_\__,_|\__\___/ Vote
        """.format(__author__, __TEAM__)
list = []
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray


def pepong():
    cek = requests.session()
    dic = {}
    count = 0    
    page = cek.get("https://free-proxy-list.net").text
    proxy = findall(r"\d+\.\d+\.\d+\.\d+",page)
    port = findall(r"\**<td>\d+</td>", page)
    for i in range(len(proxy)):
        count += 1
        ports = port[i].replace("<td>", "").replace("</td>", "")
        print str(count)+". "+B+proxy[i]+":"+str(ports)+W
        dic.update({proxy[i]:str(ports)})        
    return dic
    
def strawpoll(pid, vote, proxy):
    with requests.session() as c:
        timeout = 10
        data = {"pid":pid, "oids":vote}
        url = "https://strawpoll.com/"+pid
        print "Cek Nama: "+vote
        proxy = {"http":"http://"+proxy,
                 "https":"https://"+proxy}
        try:
            req = c.get(url, proxies=proxy, timeout=timeout)
            h = {"Origin": "https://strawpoll.com",
                 "X-Requested-With": "XMLHttpRequest",
                 "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/7.0.185.1002 Safari/537.36",
                 "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                 "Referer": "https://strawpoll.com/"+pid,
                 "Accept-Encoding": "gzip, deflate, br",
                 "Accept-Language": "en-US,en;q=0.8"}
            resp = c.post("https://strawpoll.com/vote?", data=data, proxies=proxy, timeout=timeout, headers=h)
            print resp.text
            c.cookies.clear()
            c.cookies.keys()
        except requests.exceptions.Timeout, e:
            print e
        except requests.exceptions.ConnectionError as e:
            print e

def start(jumlah):
    n = 0
    for number in range(0,jumlah):
        print "TES TING GRAB PROXY ( %s )"+str(number)
        for proxy, port in pepong().items():
            n += 1
            proxy = proxy+":"+port
            print "==== [ PROXY TEST ] ===="
            print proxy
            strawpoll(pid,vote, proxy)
        print "Total Proxy Test: ", str(n) 
        print "==== [ FINISH ] ===="
if __name__ == "__main__":
    
    #pid = "81z11c89"
    #vote = "check20369851"
    banner()
    pid = raw_input("insert PID: ")
    vote = raw_input("insert check Vote: ")
    jml = int(raw_input("Jumlah grab: "))
    start(jml)
