from ave import Ave
from ave_voladora import AveVoladora
from ave_no_voladora import AveNoVoladora

def mostrar_ave_en_accion(ave: Ave):
    print(ave.hacer_sonido())
    if isinstance(ave, AveVoladora):
        print(ave.volar())
    elif isinstance(ave, AveNoVoladora):
        print(ave.caminar())

if __name__ == "__main__":
    ave_voladora = AveVoladora()
    ave_no_voladora = AveNoVoladora()

    mostrar_ave_en_accion(ave_voladora)
    mostrar_ave_en_accion(ave_no_voladora)