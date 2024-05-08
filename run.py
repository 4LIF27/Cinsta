#!/usr/bin/env python3
I=KeyboardInterrupt
H=Exception
F=str
D='bold royal_blue1'
C=exit
try:from rich.console import Console as A;import os as B,time,re,json,requests;from rich.panel import Panel as G
except(H,I)as E:from urllib.parse import quote;__import__('os').system(f"xdg-open https://wa.me/6283198075343?text=PREMIUM%20%3A%20{quote(F(E))}");C()
class J:
	def __init__(A):0
	def Command(E):E.Banner();A(width=71,style=D).print('[italic red]\nYou can contact the admin so you can try this script, because the Apikey website service is having problems. You have to ask the admin to activate this command manually.\n');A().input('[bold white][[bold green]WhatsApp[bold white]]');time.sleep(5.);B.system(f"xdg-open https://wa.me/6283198075343?text=Hallo%20Bang%3F%0AI%20want%20to%20buy%20the%20cinsta%20script%21");C()
	def Clear(A):B.system('cls'if B.name=='nt'else'clear');return'Sukses Membersihkan Terminal'
	def Banner(B):B.Clear();A(width=71,style=D).print('[bold red]●[bold yellow] ●[bold green] ●[bold white]\n________ .___                 __          \n\\_   ___ \\|   | ____   _______/  |______   \n/    \\  \\/|   |/    \\ /  ___/\\   __\\__  \\  \n\\     \\___|   |   |  \\___ \\  |  |  / __ \\_\n \\______  /___|___|  /____  > |__| (____  /\n        \\/         \\/     \\/            \\/ \n        \n\t   Github.com/zhukov-z\n\t   t.me/a_life07');return'Sukses Menampilkan Banner'
if __name__=='__main__':
	try:
		K=re.search('columns=(\\d+),',F(B.get_terminal_size())).group(1)
		if int(K)<71:A(width=71,style=D).print(G(f"[italic red]Harap Kecilkan Tampilan Termux Dengan Cara Mencubit Layar Dalam Aplikasi Termux, Kecilkan Panel Ini Sampai Terlihat Rapi!",title='[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Kecilkan Tampilan Termux) [bold green]<[bold yellow]<[bold red]<'));C()
		else:B.system('git pull');J().Command()
	except I:C()
	except H as E:A(width=71,style=D).print(G(f"[italic red]{F(E).title()}!",title='[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<'));C(
