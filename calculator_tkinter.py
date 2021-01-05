# TIE-02101 Ohjelmointi 1: Johdanto
# Jere Mäkinen
# 4.5.2019

# Ohjelma on laskin, jossa on neljä eri toimintoa. Laskin kykenee suorittamaan
# kahdelle luvulle muutamia peruslaskutoimtuksi, laskemaan kahden koordinaatti-
# pisteen etäisyyden, ratkaisemaan toisen asteen yhtälön ja laskemaan pinta-
# aloja yksinkertaisille kappaleille.

from tkinter import *


class Laskin:

    def __init__(self):
        self.__ikkuna = Tk()
        self.__ikkuna.title("Laskin")
        self.__ikkuna.option_add("*Font", "Times 16")

        # Ensimmäinen toiminto on peruslaskutoimitukset. Tämä sisältää summan,
        # erotuksen, tulon, osamäärän ja potenssiin korotuksen sekä juuren las-
        # laskemisen

        self.__toiminto1 = Label(self.__ikkuna, text="Peruslaskutoimitukset",
                                 background="black", foreground="white")
        self.__toiminto1.grid(row=1, column=1, columnspan=8)

        self.__a1 = Label(self.__ikkuna, text="a =")
        self.__a1.grid(row=3, column=1, columnspan=2)

        self.__b1 = Label(self.__ikkuna, text="b =")
        self.__b1.grid(row=3, column=5, columnspan=2)

        self.__a1_syöte = Entry()
        self.__a1_syöte.grid(row=4, column=1, columnspan=1)

        self.__laskutoimitus = Label(self.__ikkuna, text="?")
        self.__laskutoimitus.grid(row=4, column=3, columnspan=2)

        self.__b1_syöte = Entry()
        self.__b1_syöte.grid(row=4, column=5, columnspan=2)

        self.__tulos1_teksti = Label(self.__ikkuna, text="=")
        self.__tulos1_teksti.grid(row=4, column=8, columnspan=2)

        self.__tulos1 = Entry()
        self.__tulos1.grid(row=4, column=10, columnspan=2)

        self.__virhe1 = Label(self.__ikkuna, text="", foreground="red")
        self.__virhe1.grid(row=5, column=1, columnspan=8)

        self.__plussa = Button(self.__ikkuna, text="a + b", command=self.summa)
        self.__plussa.grid(row=6, column=1, columnspan=2)

        self.__miinus = Button(self.__ikkuna, text="a - b",
                               command=self.erotus)
        self.__miinus.grid(row=6, column=3, columnspan=2)

        self.__kertolasku = Button(self.__ikkuna, text="a * b",
                                   command=self.tulo)
        self.__kertolasku.grid(row=6, column=5, columnspan=2)

        self.__jakolasku = Button(self.__ikkuna, text="a / b",
                                  command=self.osamäärä)
        self.__jakolasku.grid(row=7, column=1, columnspan=2)

        self.__potenssi = Button(self.__ikkuna, text="a ^ b",
                                 command=self.potenssi)
        self.__potenssi.grid(row=7, column=3, columnspan=2)

        self.__juuri = Button(self.__ikkuna, text="a ^ (1/b)",
                              command=self.juuri)
        self.__juuri.grid(row=7, column=5, columnspan=2)

        # Toinen toiminto on koordinaattipisteiden välisen etäisyyden laskemi-
        # nen.

        self.__toiminto2 = Label(self.__ikkuna,
                                 text="Pisteiden välinen etäisyys",
                                 background="black", foreground="white")
        self.__toiminto2.grid(row=1, column=20, columnspan=8)

        self.__x1 = Label(self.__ikkuna, text="x1=")
        self.__x1.grid(row=3, column=20, columnspan=2)

        self.__y1 = Label(self.__ikkuna, text="y1=")
        self.__y1.grid(row=3, column=23, columnspan=2)

        self.__z1 = Label(self.__ikkuna, text="z1=")
        self.__z1.grid(row=3, column=26, columnspan=2)

        self.__x1_syöte = Entry()
        self.__x1_syöte.grid(row=3, column=22)

        self.__y1_syöte = Entry()
        self.__y1_syöte.grid(row=3, column=25)

        self.__z1_syöte = Entry()
        self.__z1_syöte.grid(row=3, column=28)

        self.__x2 = Label(self.__ikkuna, text="x2=")
        self.__x2.grid(row=4, column=20, columnspan=2)

        self.__y2 = Label(self.__ikkuna, text="y2=")
        self.__y2.grid(row=4, column=23, columnspan=2)

        self.__z2 = Label(self.__ikkuna, text="z2=")
        self.__z2.grid(row=4, column=26, columnspan=2)

        self.__x2_syöte = Entry()
        self.__x2_syöte.grid(row=4, column=22)

        self.__y2_syöte = Entry()
        self.__y2_syöte.grid(row=4, column=25)

        self.__z2_syöte = Entry()
        self.__z2_syöte.grid(row=4, column=28)

        self.__tulos2_laske = Button(self.__ikkuna, text="etäisyys: ",
                                     command=self.pisteiden_välinen_etäisyys)
        self.__tulos2_laske.grid(row=6, column=22)

        self.__tulos2 = Entry()
        self.__tulos2.grid(row=6, column=25, columnspan=2)

        self.__virhe2 = Label(self.__ikkuna, text="", foreground="red")
        self.__virhe2.grid(row=5, column=20, columnspan=8)

        # Kolmas toiminto on toisen asteen yhtälön ratkaiseminen.

        self.__toiminto3 = Label(self.__ikkuna,
                                 text="2. asteen yhtälön ratkaisu",
                                 background="black", foreground="white")
        self.__toiminto3.grid(row=10, column=1, columnspan=8)

        self.__toisen_asteen_termi = Label(self.__ikkuna, text="x^2 +")
        self.__toisen_asteen_termi.grid(row=12, column=3, columnspan=2)

        self.__toisen_asteen_termin_kerroin = Entry()
        self.__toisen_asteen_termin_kerroin.grid(row=12, column=1,
                                                 columnspan=2)

        self.__ensimmäisen_asteen_termi = Label(self.__ikkuna, text="x +")
        self.__ensimmäisen_asteen_termi.grid(row=12, column=8, columnspan=2)

        self.__ensimmäisen_asteen_termin_kerroin = Entry()
        self.__ensimmäisen_asteen_termin_kerroin.grid(row=12, column=6,
                                                      columnspan=2)

        self.__vakiotermi = Entry()
        self.__vakiotermi.grid(row=12, column=10, columnspan=2)

        self.__yhtälön_toinen_puoli = Label(self.__ikkuna, text=" = 0")
        self.__yhtälön_toinen_puoli.grid(row=12, column=12, columnspan=2)

        self.__tulos3_teksti = Button(self.__ikkuna, text="ratkaisu(t): ",
                                      command=self.toisen_asteen_yhtälö)
        self.__tulos3_teksti.grid(row=14, column=1, columnspan=4, sticky=N)

        self.__tulos3 = Entry()
        self.__tulos3.grid(row=14, column=5, columnspan=2, sticky=N)

        self.__virhe3 = Label(self.__ikkuna, text="", foreground="red")
        self.__virhe3.grid(row=13, column=1, columnspan=8)

        # Neljäs toiminto on pinta-alan laskeminen. Valittavia muotoja ovat
        # ympyrä, suorakulmio ja kolmio.

        self.__toiminto4 = Label(self.__ikkuna, text="Pinta-alalaskuri",
                                 background="black", foreground="white")
        self.__toiminto4.grid(row=10, column=20, columnspan=8)

        # Määritellään kuvat painikkeisiin eri kuvioille.

        self.__ympyrän_kuva = PhotoImage(file="circle.gif")
        self.__suorakulmion_kuva = PhotoImage(file="square.gif")
        self.__kolmion_kuva = PhotoImage(file="triangle.gif")

        self.__a2 = Label(self.__ikkuna, text="a =")
        self.__a2.grid(row=12, column=20, columnspan=2, sticky=E)

        self.__a2_syöte = Entry()
        self.__a2_syöte.grid(row=12, column=22)

        self.__b2 = Label(self.__ikkuna, text="b =")
        self.__b2.grid(row=12, column=26, columnspan=2, sticky=E)

        self.__b2_syöte = Entry()
        self.__b2_syöte.grid(row=12, column=28)

        self.__valitse_kuvio = Label(self.__ikkuna, text="Valitse kuvio:")
        self.__valitse_kuvio.grid(row=15, column=20, columnspan=8)

        self.__ympyrä = Button(self.__ikkuna, image=self.__ympyrän_kuva,
                               command=self.ympyrän_ala)
        self.__ympyrä.grid(row=16, column=20, columnspan=4)

        self.__suorakulmio = Button(self.__ikkuna,
                                    image=self.__suorakulmion_kuva,
                                    command=self.suorakulmion_ala)
        self.__suorakulmio.grid(row=16, column=24, columnspan=4, sticky=W)

        self.__kolmio = Button(self.__ikkuna, image=self.__kolmion_kuva,
                               command=self.kolmion_ala)
        self.__kolmio.grid(row=16, column=28, columnspan=4, sticky=W)

        self.__tulos4_teksti = Label(self.__ikkuna, text="pinta-ala:")
        self.__tulos4_teksti.grid(row=14, column=20, columnspan=2)

        self.__tulos4 = Entry()
        self.__tulos4.grid(row=14, column=22)

        self.__virhe4 = Label(self.__ikkuna, text="", foreground="red")
        self.__virhe4.grid(row=13, column=20, columnspan=8)

        # Lopeta-nappi lopettaa laskimen käytön.

        self.__lopeta = Button(self.__ikkuna, text="Lopeta",
                               command=self.lopeta)
        self.__lopeta.grid(row=1, column=40)

        self.__ikkuna.mainloop()

    # Metodi laskee kahden käyttäjän syöttämän luvun summan. Jos syötteet ovat
    # vääränlaiset tulostetaan virhekenttään ilmoitus.

    def summa(self):

        try:
            a = self.__a1_syöte.get()
            b = self.__b1_syöte.get()
            summa = float(a) + float(b)
            tulos = "{}".format(summa)
            self.__tulos1.delete(0, END)
            self.__tulos1.insert(0, tulos)
            self.__virhe1.configure(text="")
        except ValueError:
            self.__virhe1.configure(text="Syötä kokonais- tai desimaililukuja")
            self.__tulos1.delete(0, END)

    # Metodi laskee kahden käyttäjän syöttämän luvun erotuksen. Jos syötteet
    # ovat vääränlaiset tulostetaan virhekenttään ilmoitus.

    def erotus(self):

        try:
            a = self.__a1_syöte.get()
            b = self.__b1_syöte.get()
            erotus = float(a) - float(b)
            tulos = "{}".format(erotus)
            self.__tulos1.delete(0, END)
            self.__tulos1.insert(0, tulos)
            self.__virhe1.configure(text="")
        except ValueError:
            self.__virhe1.configure(text="Syötä kokonais- tai desimaililukuja")
            self.__tulos1.delete(0, END)

    # Metodi laskee kahden käyttäjän syöttämän luvun tulon. Jos syötteet
    # ovat vääränlaiset tulostetaan virhekenttään ilmoitus.

    def tulo(self):

        try:
            a = self.__a1_syöte.get()
            b = self.__b1_syöte.get()
            tulo = float(a) * float(b)
            tulos = "{}".format(tulo)
            self.__tulos1.delete(0, END)
            self.__tulos1.insert(0, tulos)
            self.__virhe1.configure(text="")
        except ValueError:
            self.__virhe1.configure(text="Syötä kokonais- tai desimaililukuja")
            self.__tulos1.delete(0, END)

    # Metodi laskee kahden käyttäjän syöttämän luvun osamäärän. Jos syötteet
    # ovat vääränlaiset tulostetaan virhekenttään ilmoitus. Virheilmoitus anne-
    # taan myös kun jakajaksi on syötetty nolla.

    def osamäärä(self):

        try:
            a = self.__a1_syöte.get()
            b = self.__b1_syöte.get()
            if float(b) == 0:
                self.__virhe1.configure(text="Nollalla ei voi jakaa")
            else:
                osamäärä = float(a) / float(b)
                tulos = "{}".format(osamäärä)
                self.__tulos1.delete(0, END)
                self.__tulos1.insert(0, tulos)
                self.__virhe1.configure(text="")
        except ValueError:
            self.__virhe1.configure(text="Syötä kokonais- tai desimaililukuja")
            self.__tulos1.delete(0, END)

    # Metodi korottaa a:n b:teen potenssiin. Jos syötteet ovat vääränlaiset tu-
    # tulostuu virhekenttään ilmoitus.

    def potenssi(self):

        try:
            a = self.__a1_syöte.get()
            b = self.__b1_syöte.get()
            tulos = float(a) ** float(b)
            tulos = "{}".format(tulos)
            self.__tulos1.delete(0, END)
            self.__tulos1.insert(0, tulos)
            self.__virhe1.configure(text="")
        except ValueError:
            self.__virhe1.configure(text="Syötä kokonais- tai desimaililukuja")
            self.__tulos1.delete(0, END)

    # Metodi laskee a:n b:nnen juuren. Jos syötteet ovat vääränlaiset tuloste-
    # taan virhekenttään ilmoitus. Virheilmoitus annetaan myös kun jakajaksi on
    # syötetty nolla.

    def juuri(self):

        try:
            a = self.__a1_syöte.get()
            b = self.__b1_syöte.get()
            if float(b) == 0:
                self.__virhe1.configure(text="Nollalla ei voi jakaa")
            else:
                tulos = float(a) ** (1 / float(b))
                tulos = "{}".format(tulos)
                self.__tulos1.delete(0, END)
                self.__tulos1.insert(0, tulos)
                self.__virhe1.configure(text="")
        except ValueError:
            self.__virhe1.configure(text="Syötä kokonais- tai desimaililukuja")
            self.__tulos1.delete(0, END)

    # Metodi laskee kahden koordinaattipisteen välisen etäisyyden. Jos syötteet
    # ovat vääränlaiset tulostuu virhekenttään ilmoitus. Metodi tulkitsee tyh-
    # jät ruudut nolliksi, jotta etäisyyksien laskeminen muissakin kuin xyz-
    # koordinaatistoissa helpottuisi.

    def pisteiden_välinen_etäisyys(self):

        try:
            x1 = self.__x1_syöte.get()
            if x1 == "":
                x1 = 0
            else:
                x1 = float(self.__x1_syöte.get())

            x2 = self.__x2_syöte.get()
            if x2 == "":
                x2 = 0
            else:
                x2 = float(self.__x2_syöte.get())

            y1 = self.__y1_syöte.get()
            if y1 == "":
                y1 = 0
            else:
                y1 = float(self.__y1_syöte.get())

            y2 = self.__y2_syöte.get()
            if y2 == "":
                y2 = 0
            else:
                y2 = float(self.__y2_syöte.get())

            z1 = self.__z1_syöte.get()
            if z1 == "":
                z1 = 0
            else:
                z1 = float(self.__z1_syöte.get())

            z2 = self.__z2_syöte.get()
            if z2 == "":
                z2 = 0
            else:
                z2 = float(self.__z2_syöte.get())

            x = x2 - x1
            y = y2 - y1
            z = z2 - z1

            d = (x**2 + y**2 + z**2) ** 0.5
            etäisyys = "{}".format(d)

            self.__tulos2.delete(0, END)
            self.__tulos2.insert(0, etäisyys)

        except ValueError:
            self.__virhe2.configure(text="Syötä kokonais- tai desimaililukuja")
            self.__tulos2.delete(0, END)

    # Metodi ratkaisee toisen asteen yhtälön käyttäjän syöttämien kertoimien
    # perusteella. Virheilmoitus tulostuu jos kaikki kertoimet ovat nollia tai
    # syötteet epäsopivia. Jos kaikki ruudut eivät ole tyhjiä tulkitaan tyhjä
    # ruutu nollaksi. Yhtälö tulostaa tilanteesta riipuen yhtälön ratkaisut tai
    # ratkaisun ja ilmoittaa mikäli ratkaisuja ei ole.

    def toisen_asteen_yhtälö(self):

        try:
            a = self.__toisen_asteen_termin_kerroin.get()
            if a == "":
                a = 0
            else:
                a = float(self.__toisen_asteen_termin_kerroin.get())

            b = self.__ensimmäisen_asteen_termin_kerroin.get()
            if b == "":
                b = 0
            else:
                b = float(self.__ensimmäisen_asteen_termin_kerroin.get())

            c = self.__vakiotermi.get()
            if c == "":
                c = 0
            else:
                c = float(self.__vakiotermi.get())

            if a == 0 and b == 0 and c == 0:
                self.__virhe3.configure(text="Syötä yhtälöön kertoimet")
                self.__tulos3.delete(0, END)

            elif a == 0 and b == 0:
                self.__virhe3.configure(text="")
                self.__tulos3.delete(0, END)
                self.__tulos3.insert(0, "Ei ratkaisuja")

            elif a == 0:
                ratkaisu = -c / b
                self.__virhe3.configure(text="")
                self.__tulos3.delete(0, END)
                self.__tulos3.insert(0, "x = {:.4f}".format(ratkaisu))

            else:
                diskriminantti = b**2 - 4*a*c

                if diskriminantti < 0:
                    self.__virhe3.configure(text="")
                    self.__tulos3.delete(0, END)
                    self.__tulos3.insert(0, "Ei ratkaisuja")

                elif diskriminantti == 0:
                    ratkaisu = -b / (2*a)
                    self.__virhe3.configure(text="")
                    self.__tulos3.delete(0, END)
                    self.__tulos3.insert(0, "x = {:.4f}".format(ratkaisu))

                elif diskriminantti > 0:
                    ratkaisu1 = (-b + (b**2 - 4*a*c)**0.5) / (2 * a)
                    ratkaisu2 = (-b - (b**2 - 4*a*c)**0.5) / (2 * a)
                    self.__virhe3.configure(text="")
                    self.__tulos3.delete(0, END)
                    self.__tulos3.insert(0, "x = {:.4f} tai x = {:.4f}"
                                         .format(ratkaisu1, ratkaisu2))

        except ValueError:
            self.__virhe3.configure(text="Syötä kokonais- tai desimaililukuja")
            self.__tulos3.delete(0, END)

    # Metodi laskee ympyrän pinta-alan käyttäjän syöttämän säteen perusteella.
    # Jos syöte on vääränlainen siitä tulostuu ilmoitus.

    def ympyrän_ala(self):

        try:
            pi = 3.14159265358979323846264338327950
            säde = float(self.__a2_syöte.get())
            ala = pi*säde**2
            tulos = "{:.4f}".format(ala)
            self.__virhe4.configure(text="")
            self.__tulos4.delete(0, END)
            self.__tulos4.insert(0, tulos)

        except ValueError:
            self.__virhe4.configure(text="Syötä kokonais- tai desimaililukuja")
            self.__tulos4.delete(0, END)

    # Metodi laskee suorakulmion pinta-alan käyttäjän syöttämillä kantojen
    # pituuksilla. Vääränlaisista syötteistä tulostuu virheilmoitus.

    def suorakulmion_ala(self):

        try:
            a = float(self.__a2_syöte.get())
            b = float(self.__b2_syöte.get())
            ala = a * b
            tulos = "{:.4f}".format(ala)
            self.__virhe4.configure(text="")
            self.__tulos4.delete(0, END)
            self.__tulos4.insert(0, tulos)

        except ValueError:
            self.__virhe4.configure(text="Syötä kokonais- tai desimaililukuja")
            self.__tulos4.delete(0, END)

    # Metodi laskee kolmion pinta-alan käyttäjän syöttämästä korkeudesta ja
    # kannasta. Vääränlaisista syötteistä tulostuu virheilmoitus.

    def kolmion_ala(self):

        try:
            kanta = float(self.__a2_syöte.get())
            korkeus = float(self.__b2_syöte.get())
            ala = 0.5 * kanta * korkeus
            tulos = "{:.4f}".format(ala)
            self.__virhe4.configure(text="")
            self.__tulos4.delete(0, END)
            self.__tulos4.insert(0, tulos)

        except ValueError:
            self.__virhe4.configure(text="Syötä kokonais- tai desimaililukuja")
            self.__tulos4.delete(0, END)

    def lopeta(self):
        self.__ikkuna.destroy()


def main():
    Laskin()


main()
