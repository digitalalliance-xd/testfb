import requests, os, re, random, time, sys, json
from data import logo as asy

#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.panel import Panel

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
warna = random.choice(["[deep_pink3]","[green]","[cyan]","[blue]"])
#-------- LOADING ANIMASI -----------
class Login:

    def __init__(self):
        asy.Logo().log()
        self.login_cookie()

    def loading(self):
        animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
        print("")
        for i in range(50):
            time.sleep(0.1)
            sys.stdout.write(f"\r  {N}[{O}•{N}] {H}proses...{N} " + animation[i % len(animation)] +"\x1b[0m ")
            sys.stdout.flush()
        print()

    def login_cookie(self):
        prints(Panel("[[green]•[/]] masukan cookie facebook anda"))
        coki = input(f"  [{O}?{N}] cookie fb :{H} ")
        self.loading()
        try:
            get_tok = requests.get("https://business.facebook.com/business_locations",headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":coki})
            token = re.search("(EAAG\w+)", get_tok.text).group(1)
            cookie = {'cookie': coki}
            get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
            jsx = json.loads(get.text)
            nama = jsx["name"]
            open('.token.txt', 'a').write(token)
            open('.cokie.txt', 'a').write(coki)
            prints(Panel(f"""[[green]✓[/]] LOGIN SUCCESS"""));time.sleep(0.3)
            os.system('run.py')
        except requests.exceptions.ConnectionError:
            prints(Panel("😭[bold red] Tidak ada koneksi internet"));exit()
        except (KeyError,IOError,AttributeError):
           prints(Panel("😔[bold red] Cookie kamu invalid"));exit()