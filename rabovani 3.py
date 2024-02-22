import random
import sys
import turtle

hrac = turtle.Turtle()
plan = turtle.Screen()
plan.bgpic("oc.gif")
hrac.up()
hrac.goto(10,-240)


print("**********")
print("jednoho dne civilizovany svet, ve kterem jsi zil, prestal existovat")
print("uz se asi nikdy nedozvis, proc se to stalo, ale jsi odhodlan prezit")
print("ve meste neni bezpecno, a tak jsi chtel utect na venkov")
print("shromazdil sis doma veci potrebne pro preziti, ale ale loupeziva tlupa te o ne pripravila")
print("nezbyva ti tedy nez zkusit prohledat mistni obchodni centrum a najit neco uzitecneho")
print("nebude to lehke, protoze jdes v noci a musis si dat pozor na dalsi lidi...")
print("**********")

hraciPole = [1,2,3,4,5,6,7,8,9]
tvojePoloha = 0

x = random.randint(0,8)
i = hraciPole[x]
del hraciPole[x]
x = random.randint(0,7)
a = hraciPole[x]
del hraciPole[x]
x = random.randint(0,6)
b = hraciPole[x]
del hraciPole[x]
x = random.randint(0,5)
c = hraciPole[x]
del hraciPole[x]
x = random.randint(0,4)
d = hraciPole[x]
del hraciPole[x]
x = random.randint(0,3)
e = hraciPole[x]
del hraciPole[x]
x = random.randint(0,2)
f = hraciPole[x]
del hraciPole[x]
x = random.randint(0,1)
g = hraciPole[x]
del hraciPole[x]
h = hraciPole[0]


class Obchod:

    def __init__(self, nazev, poloha, veci, penize): 
        self.nazev = nazev
        self.poloha = poloha
        self.veci = veci
        self.penize = penize

Ob1 = Obchod("Potraviny", a, "konzerva", 0)

Ob2 = Obchod("Lékárna", b, "Aspirin", 500)

Ob3 = Obchod("Nářadí", c,"hřebíky", 0)

Ob4 = Obchod("obchod s blečením", d, "nepromokavá bunda", 200)

Ob5 = Obchod("kadeřnictví", e, "jenom smetí", 500)

Ob6 = Obchod("obchod s outdoorovým vybavením", f, "filtr na vodu", 0)

Ob7 = Obchod("Drogérie", g, "jenom smetí", 1000)

Ob8 = Obchod("Trafika", h, "zapalovač", 0)

Ob9 = Obchod("knihkupectví", i, "jenom smetí", 700)



OC = [Ob1, Ob2, Ob3, Ob4, Ob5, Ob6, Ob7, Ob8, Ob9]
batoh = []
penezenka = 0
kola = 0

def kde():
    for v in OC:
        if tvojePoloha == v.poloha:
            return v

def boj():
    global penezenka
    print("Pred tebou nekdo stoji!")
    print("chces se pokusit zabranit konfliktu tim, ze pred nej hodis vsechny sve penize a uteces?")
    z = input("ano(a) ne(n): ")
    while z not in ["a", "n"]:
        z = input("a nebo n: ")
    if z == "a":
        if penezenka > 0:
            print(f"vyvazl jsi... jen skoda tech {penezenka} korun")
            penezenka = 0
            return
        else:
            print("sakra! zadne penize nemas...")
    
    print("postava se k tobe pomalu blizi")
    print("potom te bez varovani srazi na zem")
    l = random.randint(1,2)
    if l == 1:
        print("rychle ses vzpamatoval a zacal se branit")
        print("ukazalo se, ze jsi o neco silnejsi nez tvuj protivnik")
        print("podarilo se ti ho omracit")
        q = input("chces prohledat co ma v kapsach? ano(a) ne(n): ")
        while q not in ["a", "n"]:
            q = input("a nebo n: ")
        if q == "a":
            print("vida! nasel jsi klice od auta a 2000 korun")
            penezenka += 2000
            batoh.append("klice od auta")
        print("rychle se vzdalujes od tela, protoze z toho mas neprijemny pocit")

    else:
        print("uderi te do hlavy")
        print("citis, jak te pomalu opousti vedomi...")
        print("*************")
        print("KONEC HRY")
        sys.exit()



def pohyb():
    global tvojePoloha
    mv = input("kam chces jit? s,j,v,z: ")
    if mv == "s" and tvojePoloha in [1,2,3,4]:
        tvojePoloha += 1
    elif mv == "s" and tvojePoloha in [6,7,8,9]:
        tvojePoloha -= 1
    elif mv == "j" and tvojePoloha in [2,3,4]:
        tvojePoloha -= 1
    elif mv == "j" and tvojePoloha in [6,7,8]:
        tvojePoloha += 1
    elif mv == "z" and tvojePoloha == 0:
        tvojePoloha = 9
    elif mv == "z" and tvojePoloha == 3:
        tvojePoloha = 8
    elif mv == "z" and tvojePoloha == 5:
        tvojePoloha = 6
    elif mv == "z" and tvojePoloha == 1:
        tvojePoloha = 9
    elif mv == "v" and tvojePoloha == 0:
        tvojePoloha = 1
    elif mv == "v" and tvojePoloha == 5:
        tvojePoloha = 4
    elif mv == "v" and tvojePoloha == 8:
        tvojePoloha = 3
    elif mv == "v" and tvojePoloha == 9:
        tvojePoloha = 1
    elif mv == "j" and (tvojePoloha == 1 or tvojePoloha == 9):
        if ("konzerva" and "Aspirin" and "hřebíky" and "nepromokavá bunda" and "filtr na vodu" and "zapalovač" and "klice od auta") in batoh:
            tvojePoloha = 0
            hrac.goto(10,-270)
            print("vyborne! mas vsechno a uz ti nic nebrani odejit")
            print("na parkovisti jsi nasel auto patrici k ukradenym klickum")
            print("k tvemu stesti melo plnou nadrz")
            print("ujel jsi do bezpeci...")
            print("**************")
            print("KONEC HRY")
            sys.exit()
        else:
            print("jeste nemas vsechny uzitecne veci, ktere tady muzes sehnat")
            pohyb()
        
    else:
        print("tenhle pohyb nejde. podivej se na mapu")
        pohyb()
    
def kresleni():
    global tvojePoloha
    global kola
    if tvojePoloha == 0 and kola > 1:
        hrac.goto(10,-240)
    elif tvojePoloha == 1:
        hrac.goto(110,-170)
    elif tvojePoloha == 2:
        hrac.goto(155,-100)
    elif tvojePoloha == 3:
        hrac.goto(170,0)
    elif tvojePoloha == 4:
        hrac.goto(160,120)
    elif tvojePoloha == 5:
        hrac.goto(0,240)
    elif tvojePoloha == 6:
        hrac.goto(-130,130)
    elif tvojePoloha == 7:
        hrac.goto(-160,40)
    elif tvojePoloha == 8:
        hrac.goto(-160,-70)
    elif tvojePoloha == 9:
        hrac.goto(-90,-180)
    else:
        return    
       


def kolo():
    print(" ")
    print(" ")
    print("***************")
    print(" ")
    print(" ")
    global tvojePoloha
    global kola
    print(f"obsah tveho batohu: {batoh}")
    global penezenka
    print(f"mas {penezenka} korun")
    kola += 1

    pohyb()
    kresleni()

    w = random.randint(1,2)
    if w == 2:
        print("ve tme se ozyva nejaky sramot. Mohlo by to byt nebezpecne...")
        
    n = input("chces prohledat obchod vedle tebe? ano(a) ne(n): ")
    while n not in ["a", "n"]:
        n = input("a nebo n: ")
    if n == "a":
        print("jsi uvnitr")
        x = random.randint(1,3)
        if x * w >= 3 and kola > 3:
            boj()
        print(f"vypada to tady jako {kde().nazev}")
        print(f"na zemi lezi {kde().veci}")
        
        if kde().veci != "jenom smetí":
            r = input("chces si to dat do batohu? ano(a) ne(n): ")
            while r not in ["a", "n"]:
                r = input("a nebo n: ")
            if r == "a":
                batoh.append(kde().veci)
                kde().veci = "jenom smetí"
        
        k = input("chces se podivat ke kase? ano(a) ne(n): ")
        while k not in ["a", "n"]:
            k = input("a nebo n: ")
        if k == "a":
            print(f"je tady {kde().penize} korun")
            if kde().penize > 0:
                m = input("chces je vzit? ano(a) ne(n): ")
                while m not in ["a", "n"]:
                    m = input("a nebo n: ")
                if m == "a":
                    penezenka += kde().penize
                    kde().penize = 0
                    
        print("vychazis ven")
        kolo()
    else:
        kolo()
    

kolo()            
