class cliente():
    def __init__(self, hab, nombre, ciudad, dias, forma, can=1):
        self.hab = hab
        self.nombre = nombre
        self.ciudad = ciudad
        self.dias = dias
        self.forma = forma
        self.can = can
    
    @property
    def total(self):
        match self.hab:
            case 1 | 2 | 3: return self.dias * 1000
            case 4 | 5 | 6: return self.dias * 1500
            case 7 | 8 | 9: return self.dias * self.can * 500
    
    def cinfo(self):
         return f"\nNombre: {self.nombre}\nCiudad: {self.ciudad}\nEstancia: {self.dias}\nTotal: {self.total}\nForma de pago: {self.forma}\n"

class hotel():
    def __init__(self):
        self.habitaciones = {}

    def registro(self, hab, nombre, ciudad, dias, forma, can=1):
            if hab in self.habitaciones: print("Habitación ocupada") ; return
            self.habitaciones[hab] = cliente(hab, nombre, ciudad, dias, forma, can)
            guardar(self.habitaciones)

    def busqueda(self, hab):
         if hab in self.habitaciones: print(self.habitaciones[hab].cinfo())
         else: print("Habitación vacía")

    def tabla(self):
        print(); print(f"{"Habitaciones:":<15}", end=" ")
        for i in range(1,10): print(i,end=" ")
        print() ; print(f"{"Ocupadas:":<15}", end=" ")
        for i in range(1,10): print(1 if i in self.habitaciones else 0, end=" ")
        print("\n")
              
    def mod(self, hab, dias_n):
        if hab not in self.habitaciones: print("Habitación vacía") ; return
        self.habitaciones[hab].dias = dias_n
        guardar(self.habitaciones)

    def eliminar(self, hab):
        if hab not in self.habitaciones: print("Habitación vacía") ; return
        self.habitaciones.pop(hab)
        guardar(self.habitaciones)

    def ingresos(self):
        with open("python/Proyecto_final/informe.txt","a") as f:
            texto = f"INGRESOS TOTALES: {sum(x.total for x in self.habitaciones.values())}"
            print(f"{texto:^140}", file=f)
            print("-"*140, file = f)
                                  
def guardar(datos):
     with open("python/Proyecto_final/informe.txt","w") as f:
        print("-"*140, file = f)
        print(f"{"HABITACION":^20}{"NOMBRE":^20}{"CIUDAD":^20}{"ESTANCIA":^20}{"NUM.P":^20}{"TOTAL":^20}{"PAGO":^20}", file = f)
        print("-"*140, file = f)
        for hab, cliente in datos.items(): 
            print(f"{hab:^20}{cliente.nombre:^20}{cliente.ciudad:^20}{cliente.dias:^20}{cliente.can:^20}{cliente.total:^20}{cliente.forma:^20}", file = f)
        print("-"*140, file = f)




"""
def formato(texto, ancho = 60, ancho_barras = 60):
    print(("_" * ancho_barras).center(ancho))
    print(texto.center(ancho))
    print(("¯" * ancho_barras).center(ancho))

def elegir_opcion(texto,letra1,letra2):
    while True:
        letra = input(f"{texto} ({letra1}/{letra2}): ").replace(" ","").upper()
        if letra == letra1: return True
        elif letra == letra2: return False
        else: print(f"El valor {letra} es invalido, intenta otra vez.\n")

def main():
    h = hotel()
    formato("HOTEL - PROYECTO FINAL")
    print("1.-Registro\n2.-Búsqueda\n3.-Reportes")
    print("4.-Modificaciones\n5.-Eliminar\n6.-Salir\n")
    while True:
        match input("Ingresa la opción: "):
            case "1": 
                o = input("Ingresa (Habitación Nombre Ciudad Estancia Forma de Pago Np): ").split()  
                h.registro(int(o[0]), o[1], o[2], int(o[3]), o[4], int(o[5]))
                formato("")
            case "2": h.busqueda(int(input("Ingresa la habitación: "))); formato("")
            case "3": h.tabla() ; formato("")
            case "4": 
                a,b = map(int, input("Ingresa la habitación y el nuevo valor(a,b): ").split())
                h.mod(a,b) ; formato("")
            case "5": h.eliminar(int(input("Ingresa el registro al que eleminar: ")))
            case "6": formato("GRACIAS POR SU TIEMPO"); h.ingresos(); break
    
if __name__ == "__main__":
    main()
"""
#1 Yolotl Puebla 3 Efectivo 1
#2 Ana Puebla 4 Tarjeta 1
#3 Carlos CDMX 7 Tarjeta 1
#4 Juan Tlaxcala 2 Efectivo 1
#5 Pedro Oaxaca 5 Tarjeta 1
#6 Lucia Merida 3 Efectivo 1
#7 Mario Puebla 4 Tarjeta 6
#8 Sofia CDMX 6 Efectivo 3
#9 Luis Tlaxcala 1 Tarjeta 4