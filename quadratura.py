from sympy import *
import math
class Quadratura():
    def __init__(self):
        [self.f_symb, self.f, self.a, self.b] = self.set_data()

    def set_function(self):
        x = symbols("x")
        f_symb = sympify(input("Inserisci la funzione: "))  # converte la stringa in funzione simbolica
        f = lambdify(x, f_symb)  # trasforma la funzione simbolica in espressione matematica
        return f_symb, f

    def vett(self, f, a, b, h):  # crea il vettore x dei nodi, da a a b spaziati di h e il vettore fx, contenente tutti i valori che f assume nei nodi (approssimazione a 4 cifre dopo la virgola)
        # che per ogni i è uguale a f(v(i))
        x = []
        fx = []
        k = a
        while k <= b:
            x.append(k)
            k = round(k+h, 4)
        if b not in x:
            x.append(b)
        for i in range(len(x)):  # len(v) = len(fx) = N + 1
            fx.append(round(f(x[i]), 4))
        return x, fx
    def set_data(self):
        f_symb, f = self.set_function()
        a = float(input("Inserisci l'estremo sinistro dell'intervallo: "))
        b = self.set_b(a)
        return f_symb, f, a, b
    def set_b(self, a):
        b = float(input("Estremo destro dell'intervallo: "))
        if b == a or b < a:
            print("L'estremo b è uguale all'estremo a. Riprova.")
            self.set_b(a)
        return b
    def get_M(self, f_symb, a, b, n): #n rappresenta il grado della derivata
        v = []
        x = symbols("x")
        devf = lambdify(x, diff(f_symb, x, n))
        v.append(abs(devf(a)))
        v.append(abs(devf(b)))
        return max(v)

    def trapezi_semplice(self, f_symb, f, a, b):
        h = b - a
        M = self.get_M(f_symb, a, b, 2)
        valore = (h/2) * (f(a) + f(b))
        resto = -((h ** 3) * M)/12
        print(f"Valore dell'integrale: {round(valore, 4)} con un resto di {round(resto, 4)}")
        return valore

    def trapezi_composta(self, f_symb, f, a, b):
        M = self.get_M(f_symb, a, b, 2) #max valore della derivata seconda
        E = float(input("Inserisci la precisione desiderata: "))
        N = int(round(sqrt((((b - a) ** 3) * M) / (12 * E))))
        h = float((b - a) / N) # h è il valore di un sottointervallo
        x, fx = self.vett(f, a, b, h)
        valore = 0
        for i in range(N):
            valore += ((h/2) * (fx[i] + fx[i+1]))
        resto = -(((b-a)**3)*M)/(12*(N**2))
        print(f"valore dell'integrale: {round(valore, 4)} con un resto di {round(resto, 4)}")

    def simpson_semplice(self, f_symb, f, a, b):
        h = float((b-a)/2) #N = 2
        c = a + h
        M = self.get_M(f_symb, a, b, 4)
        valore = (h/3) * (f(a) + 4*f(c) + f(b))
        resto = -((h**3)*M)/90
        print(f"Valore dell'integrale: {round(valore, 4)} con un resto di {round(resto, 4)}")

    def simpson_composta(self, f_symb, f, a, b): #N deve essere pari
        M = self.get_M(f_symb, a, b, 4)
        E = float(input("Inserisci la precisione desiderata: "))
        N = math.ceil(pow((((b - a) ** 5) * M) / (180 * E), 1 / 4))  # radice quarta
        if N % 2 == 1: #N dispari
            N += 1
        h = float((b-a)/N)
        x, fx = self.vett(f, a, b, h)
        valore = 0
        for i in range(int(N/2)):
            valore += ((h/3) * (fx[2*i] + 4*fx[(2*i)+1] + fx[(2*i)+2]))
        resto = -((h**5)*N*M)/180
        print(f"valore dell'integrale: {round(valore, 4)} con un resto di {round(resto, 4)}")

    def punto_di_mezzo_semplice(self, f_symb, f, a, b):
        c = (b + a)/2 #punto di mezzo tra a e b
        h = (b - a)/2 #spaziatura tra i nodi a b c
        M = self.get_M(f_symb, a, b, 2)
        valore = (f(c)*(b-a))
        resto = ((h**3)*M)/24
        print(f"valore dell'integrale: {round(valore, 4)} con un resto di {round(resto, 4)}")

    def punto_di_mezzo_composta(self, f_symb, f, a, b):
        M = self.get_M(f_symb, a, b, 2)
        E = float(input("Inserisci la precisione desiderata: "))
        N = math.ceil(pow((((b-a)**3)*M)/(24*E), 1/3))
        if N % 2 == 1:
            N += 1
        h = (b-a)/N
        x, fx = self.vett(f, a, b, h)
        valore = 0
        for i in range(int(N/2)):
            valore += (fx[(2*i)+1] * (x[(2*i)+2] - x[(2*i)]))
        print(f"valore dell'integrale: {round(valore, 4)} con un resto di {round(resto, 4)}")


