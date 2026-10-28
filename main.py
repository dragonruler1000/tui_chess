from colorama import init, Fore, Back, Style
init()

team1 = Fore.RED
team2 = Fore.BLUE

def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)

def render_board(a8,a7,a6,a5,a4,a3,a2,a1,b8,b7,b6,b5,b4,b3,b2,b1,c8,c7,c6,c5,c4,c3,c2,c1,d8,d7,d6,d5,d4,d3,d2,d1,
                 e8,e7,e6,e5,e4,e3,e2,e1,f8,f7,f6,f5,f4,f3,f2,f1,g8,g7,g6,g5,g4,g3,g2,g1,h8,h7,h6,h5,h4,h3,h2,h1):
    print("  a  b  c  d  e  f  g  h")
    print("8"+a8+b8+c8+d8+e8+f8+g8+h8+"8")
    print("7"+a7+b7+c7+d7+e7+f7+g7+h7+"7")
    print("6"+a6+b6+c6+d6+e6+f6+g6+h6+"6")
    print("5"+a5+b5+c5+d5+e5+f5+g5+h5+"5")
    print("4"+a4+b4+c4+d4+e4+f4+g4+h4+"4")
    print("3"+a3+b3+c3+d3+e3+f3+g3+h3+"3")
    print("2"+a2+b2+c2+d2+e2+f2+g2+h2+"2")
    print("1"+a1+b1+c1+d1+e1+f1+g1+h1+"1")
    print("  a  b  c  d  e  f  g  h")


a8=" R "; b8=" N "; c8=" B "; d8=" Q "; e8=" K "; f8=" B "; g8=" N "; h8=" R "
a7=b7=c7=d7=e7=f7=g7=h7=" P "
a6=b6=c6=d6=e6=f6=g6=h6=" . "
a5=b5=c5=d5=e5=f5=g5=h5=" . "
a4=b4=c4=d4=e4=f4=g4=h4=h5
a3=b3=c3=d3=e3=f3=g3=h3=h5
a2=b2=c2=d2=e2=f2=g2=h2=" p "
a1,b1,c1,d1,e1,f1,g1,h1=" r "," n "," b "," q "," k "," b "," n "," r "
render_board(a8,a7,a6,a5,a4,a3,a2,a1,b8,b7,b6,b5,b4,b3,b2,b1,c8,c7,c6,c5,c4,c3,c2,c1,d8,d7,d6,d5,d4,d3,d2,d1,
             e8,e7,e6,e5,e4,e3,e2,e1,f8,f7,f6,f5,f4,f3,f2,f1,g8,g7,g6,g5,g4,g3,g2,g1,h8,h7,h6,h5,h4,h3,h2,h1)