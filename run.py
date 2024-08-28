import requests,os,time,json

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
C = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
J = '\x1b[38;5;208m' #JINGGA
G = "\033[1;32m"
R = "\033[1;91m"
W = "\033[1;97m"
B = "\033[1;94m"

def main():
  try:
    print(f"""{N}
    \t{B} https://alif15.biz.id{N}
    \t   admin@alif15.biz.id
    
    1. login key ( {K}+ setup {N})
    2. buy key
    0. {M}Exit.{N}
    """)
    menu = input(" @cinsta\> ")
    if menu == "1":
      key = input("\n @key\> ")
      params = {'key': key,'device': 'cinsta'}
      headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',}
      try:
        kunci = requests.get('https://license.serv00.net/cek.php',params=params,headers=headers,)
        if "eror" in kunci.text:
          if "Key has expired" in kunci.text:
            exit(" your key has expired")
          elif "Device limit exceeded" in kunci.text:
            exit(" login limit ")
          else:
            exit("eror")
        elif "user" in kunci.text:
          if "Device limit exceeded" in kunci.text: 
            exit(" login limit ")
          print(" @cinsta\> welcome to cinsta member")
          #print(f"\n    name : {kunci.text}\n")
          lo = requests.get(f"https://buy.alif15.biz.id/aktivasi={key}")
          lo = "ok"
          if "ok" in lo:
            print(" kode akan exp dalam 10 menit")
            kode = lo.json()["ok"]
            print(f" code : {kode}")
            url = f'https://pastebin.com/raw/{kode}'
            response = requests.get(url)
            if response.status_code == 200:
              with open('run.py', 'wb') as f:
                f.write(response.content)
                print(" done silahkan ketik ulang,python run.py")
          else:
            exit("system eror")
  
        else:
          exit(" key invalid,please contact admin")
      except requests.exceptions.ConnectionError:
        exit(" check internet")
      pass
    elif menu == "2":
      exit("  akses web untuk melihat list harga")
    else:
      pass
  except requests.exceptions.ConnectionError:
    exit()
    
#def menu(key):
  
if __name__ == "__main__":
  main()
