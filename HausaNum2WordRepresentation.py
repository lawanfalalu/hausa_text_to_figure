from __future__ import unicode_literals

class kalma:
    def __init__(self):
        ''' Constructor for this class. '''
        self.alifiyya = ["", " dubu ", " miliyan ", " biliyan ", " tiriliyan ", " kwadiliyan ", " kwintilayan ", " sektiliyan ", " seftiliyan ", " oktiliyan ", " noniiliyan ", " desiliyan "]
        self.gomiya = ["", "", " ashirin", " talatin", " arba'in", " hamsin", " sittin", " saba'in", " tamanin", " casa'in"]
        self.daidai = ["", " ɗaya", " biyu", " uku", " huɗu", " biyar", " shida", " bakwai", " takwas", " tara"]
        self.sha = [" goma", " goma sha-ɗaya", " goma sha-biyu", " goma sha-uku", " goma sha-huɗu", " goma sha-biyar", " goma sha-shida", " goma sha-bakwai", " goma sha-takwas", " goma sha-tara"]

    def mara_digo(self, lamba):
        if lamba == 0:
            return "sifili"

        jumla = ""
        alif = 0
        while True:
            saura = int(lamba % 1000)
            if saura != 0:
                str = self.daruruwa(saura)
                majoni = ""
                if alif > 0:
                    majoni = " da "
                jumla = self.alifiyya[alif] + str + majoni + jumla

            alif = alif + 1
            lamba = int(lamba / 1000)
            if lamba <= 0:
                break
        return " ".join(jumla.split())

    def mai_digo(self, lamba):
        result =  "".join("sifili" if digit == '0' else self.daidai[int(digit)] for digit in lamba).strip()
        return ' '.join(result.split())

    def fassara(self, lamba):
        if not isinstance(lamba, (int, float)): # we makesure it is a number
            raise ValueError("Input must be a number (int or float).")

        if isinstance(lamba, float):
            cikakkiyar, nakasasshiya = str(lamba).split('.')
            cikakkiyar = self.mara_digo(int(cikakkiyar))
            nakasasshiya = self.mai_digo(nakasasshiya)
            return f"{cikakkiyar} da ɗigo {nakasasshiya}".strip()

        return self.mara_digo(lamba).strip()

    def daruruwa(self, lamba):
        jumla = ""
        saura = int(lamba % 100)
        if saura < 10:
            jumla = jumla + self.daidai[saura]
        elif saura < 20:
            jumla = jumla + self.sha[int(saura % 10)]
        else:
            majoni = ""
            if lamba % 10 > 0:
                majoni = " da"
            jumla = self.gomiya[int(saura / 10)] + majoni + self.daidai[int(saura % 10)]

        majoni = ""
        if int(lamba % 100) > 0:
            majoni = " da"

        if int(lamba / 100) > 0:
            jumla = "ɗari" + self.daidai[int(lamba / 100)] + majoni + jumla

        return jumla