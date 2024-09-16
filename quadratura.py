from sympy import *
class Quadratura():
    def __init__(self):
        [self.f_symb, self.f, self.a, self.b] = self.set_data()

    def set_function(self):
        x = symbols("x")
        f_symb = sympify(input("Inserisci la funzione: "))  # converte la stringa in funzione simbolica
        f = lambdify(x, f_symb)  # trasforma la funzione simbolica in espressione matematica
        return f_symb, f

    def set_b(self, a):
        b = float(input("Estremo destro dell'intervallo: "))
        if b == a or b < a:
            print("L'estremo b è uguale all'estremo a. Riprova.")
            self.set_b(a)
        return b

    def trapezi_semplice(self, f, a, b):
        h = b - a
        M = 1
        valore = (h / 2) * (f(a) + f(b))
        resto = -((h ** 3) * M) / 12
        print(f"Valore dell'integrale: {valore} con un errore di {resto}")

    def trapezi_composta(self, f_symb, f, a, b):
        v = []
        x = symbols("x")
        E = float(input("Inserisci la precisione desiderata: "))
        devf = lambdify(x, diff(f_symb))
        v.append(devf(a))
        v.append(devf(b))
        M = max(v)
        N = int(sqrt((((b - a) ** 3) * M) / (12 * E)))
        h = float((b - a) / N)  # h è il valore di un sottointervallo
        fx = self.vett(f, a, b, h)
        valore = ((h / 2) * (fx[0] + fx[N - 1])) + h * (sum(fx[1:N - 1]))
        resto = -((((b - a) ** 3) * M) / (12 * (N ** 2)))
        print(f"Valore dell'integrale: {valore} con {N} sottointervalli.")

    def vett(self, f, a, b, h):  # crea il vettore v con elementi da a a b spaziati di h e il vettore fx
        # che per ogni i è uguale a f(v(i))
        v = []
        fx = []
        k = a
        while k <= b:
            v.append(k)
            k += h
        print(len(v))
        for i in range(len(v)):  # len(v) = N + 1
            fx.append(f(v[i]))
        return fx

    def set_data(self):
        f_symb, f = self.set_function()
        a = float(input("Inserisci l'estremo sinistro dell'intervallo: "))
        b = self.set_b(a)
        return f_symb, f, a, b

