import pyfiglet
from termcolor import colored




def logo(text,title="",title_color="green",barcolor="red",fontuse="standard",color="red",barlength=50,comment="",comment_color="green",comment_link="",link_color="red"):
    barlength = int(barlength)
    f = pyfiglet.Figlet(font=fontuse)
    print(colored(f.renderText(text),color))
    comment = comment + " --> "+colored(comment_link,link_color)
    print(colored(comment,comment_color))
    half_bar=barlength/2
    half_bar=int(half_bar)
    if title:
        print(colored("="*half_bar,barcolor),colored(f"{title}",title_color),colored("="*half_bar,barcolor)) 
    else:
        print(colored("="*barlength,barcolor))

def font_details():
    print(pyfiglet.FigletFont.getFonts())

