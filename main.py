from quadratura import Quadratura
response = int(input("Scegli quale metodo di integrazione numerica usare: \n"
                     "1)Metodo dei trapezi semplice\n"
                     "2)Metodo dei trapezi composto\n"
                     "3)Formula di Simpson semplice\n"
                     "4)Formula di Simpson composta\n"))
Obj = Quadratura()  #f_symb f a b
if response == 1:
    Obj.trapezi_semplice()
if response == 2:
    Obj.trapezi_composta(Obj.f_symb, Obj.f, Obj.a, Obj.b)
if response == 3:
    Obj.simspon_semplice()
if response == 4:
    Obj.simpson_composta()