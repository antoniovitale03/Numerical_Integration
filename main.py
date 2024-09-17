from quadratura import Quadratura
def main():
    response = int(input("Scegli quale metodo di integrazione numerica usare: \n"
                         "1)Metodo dei trapezi semplice\n"
                         "2)Metodo dei trapezi composto\n"
                         "3)Formula di Simpson semplice\n"
                         "4)Formula di Simpson composta\n"
                         "5)Formula del punto di mezzo semplice\n"
                         "6)Formula del punto di mezzo composta\n"))
    Obj = Quadratura()  #f_symb f a b
    if response == 1:
        Obj.trapezi_semplice(Obj.f_symb, Obj.f, Obj.a, Obj.b)
    elif response == 2:
        Obj.trapezi_composta(Obj.f_symb, Obj.f, Obj.a, Obj.b)
    elif response == 3:
        Obj.simpson_semplice(Obj.f_symb, Obj.f, Obj.a, Obj.b)
    elif response == 4:
        Obj.simpson_composta(Obj.f_symb, Obj.f, Obj.a, Obj.b)
    elif response == 5:
        Obj.punto_di_mezzo_semplice(Obj.f_symb, Obj.f, Obj.a, Obj.b)
    elif response == 6:
        Obj.punto_di_mezzo_composta(Obj.f_symb, Obj.f, Obj.a, Obj.b)
    else:
        print("Input non valido.Riprova")
        main()

main()
