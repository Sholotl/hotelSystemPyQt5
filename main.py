from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QLabel, QComboBox, QLineEdit, QGridLayout
from PyQt5.QtGui import QIntValidator, QPixmap, QIcon

class Eliminar(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
        QLabel {
            font-size: 15px;
            color: #333;
        }
        QLineEdit, QComboBox {
            font-size: 15px;
            padding: 6px 8px;
            border: 1px solid #aaa;
            border-radius: 6px;
            background-color: white;
        }
        QLineEdit:focus, QComboBox:focus {
            border: 1px solid #567dff;
            outline: none;
        }
        QComboBox:hover, QLineEdit:hover {
            border: 1px solid #7a7a7a;
        }
        QComboBox::drop-down {
            width: 25px;              
            border-left: 1px solid #aaa;
            background: #e1e1e1;      
        }
        QPushButton {
            font-size: 15px;
            padding: 8px 12px;
            border-radius: 6px;
            background-color: #567dff;
            color: white;
        }
        QPushButton:hover {
            background-color: #6c8cff;
        }""")
        layout = QVBoxLayout()
        
        titulo = QLabel("Eliminar Cliente por Habitación")
        layout.addWidget(titulo)

        self.habitaciones = QComboBox() ; self.habitaciones.addItem("-")
        self.habitaciones.addItems([str(x) for x in range(1,10)]) 
        layout.addWidget(self.habitaciones)

        Boton_eliminar = QPushButton("Elminar Cliente")
        Boton_eliminar.clicked.connect(self.elimina)
        layout.addWidget(Boton_eliminar)

        self.tag_eliminar = QLabel()
        layout.addWidget(self.tag_eliminar)

        layout.addStretch()
        self.setLayout(layout)

    def elimina(self):
        if (hab := self.habitaciones.currentText()).isdecimal():
            if Hotel.eliminar(int(hab)) == "Habitación vacía": self.tag_eliminar.setText("Habitación vacía")
            else: self.tag_eliminar.setText("Habitación Eliminada")

class Modificaciones(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
        QLabel {
            font-size: 15px;
            color: #333;
        }
        QLineEdit, QComboBox {
            font-size: 15px;
            padding: 6px 8px;
            border: 1px solid #aaa;
            border-radius: 6px;
            background-color: white;
        }
        QLineEdit:focus, QComboBox:focus {
            border: 1px solid #567dff;
            outline: none;
        }
        QComboBox:hover, QLineEdit:hover {
            border: 1px solid #7a7a7a;
        }
        QComboBox::drop-down {
            width: 25px;              
            border-left: 1px solid #aaa;
            background: #e1e1e1;      
        }
        QPushButton {
            font-size: 15px;
            padding: 8px 12px;
            border-radius: 6px;
            background-color: #567dff;
            color: white;
        }
        QPushButton:hover {
            background-color: #6c8cff;
        }""")
        layout = QVBoxLayout()
        
        titulo = QLabel("Modificación de Estancia por habitación")
        layout.addWidget(titulo)

        self.habitaciones = QComboBox() ; self.habitaciones.addItem("-")
        self.habitaciones.addItems([str(x) for x in range(1,10)]) 
        layout.addWidget(self.habitaciones)

        self.dias_nuevos = QLineEdit("1")
        self.dias_nuevos.setValidator(QIntValidator())
        layout.addWidget(self.dias_nuevos)

        boton_terminar = QPushButton("Modificar")
        boton_terminar.clicked.connect(self.cambiar)
        layout.addWidget(boton_terminar)

        self.texto = QLabel()
        layout.addWidget(self.texto)
        layout.addStretch()
        self.setLayout(layout)

    def cambiar(self):
        if (hab := self.habitaciones.currentText()).isdecimal():
            hab = int(self.habitaciones.currentText())
            dias_n = int(self.dias_nuevos.text())
            if Hotel.mod(hab, dias_n) == "Habitación vacía": self.texto.setText("Habitación vacía")
            else: self.texto.setText("Modificación realizada")

class Reporte(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
        QLabel {
            font-size: 15px;
            color: #333;
            background-color: hsl(226, 15%, 90%);
            border-radius: 6px;
            padding: 3px 3px
        }
        QPushButton {
            font-size: 15px;
            padding: 8px 12px;
            border-radius: 6px;
            background-color: #567dff;
            color: white;
        }
        QPushButton:hover {
            background-color: #6c8cff;
        }""")

        layout = QVBoxLayout()
        self.rep_lay = QGridLayout()

        actualizar = QPushButton("Actualizar")
        actualizar.clicked.connect(self.actual) 

        row1 = ["Habitaciones"]
        row1.extend(map(str, range(1, 10)))

        row2 = ["Estado"]
        row2.extend(map(str, Hotel.tabla()))

        self.ref = []
        for j, texto in enumerate(row1):
            self.rep_lay.addWidget(QLabel(texto), 0, j)

        for j, texto in enumerate(row2):
            label = QLabel(texto)
            self.ref.append(label)
            self.rep_lay.addWidget(label, 1, j)

        layout.addWidget(actualizar)
        layout.addLayout(self.rep_lay)
        layout.addStretch()
        self.setLayout(layout)

    def actual(self):
        row_2 = ["Estado"]
        row_2.extend(Hotel.tabla())

        for j, texto in enumerate(row_2):
            self.ref[j].setText(texto)

class Busqueda(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
        QLabel {
            font-size: 15px;
            color: #333;
        }
        QLineEdit, QComboBox {
            font-size: 15px;
            padding: 6px 8px;
            border: 1px solid #aaa;
            border-radius: 6px;
            background-color: white;
        }
        QLineEdit:focus, QComboBox:focus {
            border: 1px solid #567dff;
            outline: none;
        }
        QComboBox:hover, QLineEdit:hover {
            border: 1px solid #7a7a7a;
        }
        QComboBox::drop-down {
            width: 25px;              
            border-left: 1px solid #aaa;
            background: #e1e1e1;      
        }""")
        layout = QVBoxLayout()
        
        titulo = QLabel("Búsqueda por Habitación")
        layout.addWidget(titulo)

        self.habitaciones = QComboBox() ; self.habitaciones.addItem("-")
        self.habitaciones.addItems([str(x) for x in range(1,10)]) 
        self.habitaciones.currentIndexChanged.connect(self.informacion) 
        layout.addWidget(self.habitaciones)

        self.info = QLabel("Ingresa la habitación")
        layout.addWidget(self.info)
        layout.addStretch()
        self.setLayout(layout)

    def informacion(self):
        if (hab := self.habitaciones.currentText()).isdecimal():
            self.info.setText(Hotel.busqueda(int(hab)))

class Sectores(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
        QLabel {
            font-size: 15px;
            color: #333;
        }
        QLineEdit, QComboBox {
            font-size: 15px;
            padding: 6px 8px;
            border: 1px solid #aaa;
            border-radius: 6px;
            background-color: white;
        }
        QLineEdit:focus, QComboBox:focus {
            border: 1px solid #567dff;
            outline: none;
        }
        QComboBox:hover, QLineEdit:hover {
            border: 1px solid #7a7a7a;
        }
        QComboBox::drop-down {
            width: 25px;              
            border-left: 1px solid #aaa;
            background: #e1e1e1;      
        }
        QPushButton {
            font-size: 15px;
            padding: 8px 12px;
            border-radius: 6px;
            background-color: #567dff;
            color: white;
        }
        QPushButton:hover {
            background-color: #6c8cff;
        }""")
        layout = QVBoxLayout()

        # row 1
        row1 = QHBoxLayout()
        layout.addLayout(row1)

        tag_habitacion = QLabel("Habitación")
        row1.addWidget(tag_habitacion)

        self.habitaciones = QComboBox()
        self.habitaciones.addItems([str(x) for x in range(1, 10)]) 
        self.habitaciones.currentIndexChanged.connect(self.cantidad_personas)
        row1.addWidget(self.habitaciones)

        self.nombre = QLineEdit()
        self.nombre.setPlaceholderText("Escribe tu nombre")
        layout.addWidget(self.nombre)

        self.ciudad = QLineEdit()
        self.ciudad.setPlaceholderText("Escribe tu ciudad de origen")
        layout.addWidget(self.ciudad)

        # row 2
        row2 = QHBoxLayout()
        layout.addLayout(row2)

        tag_dias = QLabel("Días de Estancia")
        row2.addWidget(tag_dias)

        self.dias = QLineEdit("1")
        self.dias.setValidator(QIntValidator())
        row2.addWidget(self.dias)

        self.tag_per = QLabel("Cantidad de Per.")
        row2.addWidget(self.tag_per)

        self.per = QComboBox()
        self.per.addItems([str(x) for x in range(1, 7)])
        row2.addWidget(self.per)

        self.tag_per.hide()
        self.per.hide()

        # row 3
        row3 = QHBoxLayout()
        layout.addLayout(row3)

        tag_forma = QLabel("Forma de pago")
        row3.addWidget(tag_forma)

        self.forma = QComboBox()
        self.forma.addItems(["Efectivo", "Tarjeta"])
        row3.addWidget(self.forma)

        boton_terminar = QPushButton("Reservar")
        boton_terminar.clicked.connect(self.reservar)
        layout.addWidget(boton_terminar)

        self.mensaje = QLabel()
        layout.addWidget(self.mensaje)

        self.setLayout(layout)

    def cantidad_personas(self):
        sec = self.habitaciones.currentText()
        match sec:
            case "7"|"8"|"9": 
                self.tag_per.show()
                self.per.show()
            case _:
                self.tag_per.hide()
                self.per.hide()

    def reservar(self):
        try:  
            hab = int(self.habitaciones.currentText())
            nom = self.nombre.text()
            ciudad = self.ciudad.text()
            dias = int(self.dias.text())
            forma = self.forma.currentText()
            per = int(self.per.currentText())

            Hotel.registro(hab,nom,ciudad,dias,forma,per)
            self.mensaje.setText("Reserva hecha")

        except ValueError:
            self.mensaje.setText("Habitación Ocupada")

class Registro(QWidget):
    def __init__(self):
        super().__init__()
        self.reg_lay = QVBoxLayout()
        self.header()
        self.sectores()
        self.reg_lay.addStretch()
        self.setLayout(self.reg_lay)
    
    def header(self):
        head_layout = QVBoxLayout() 

        sectores = QLabel("Habitaciones\n\n(1-3) - 1000$\n(4-6) - 1500$\n(7-10) - 500$ (Por Per.)")
        sectores.setStyleSheet("""
            QLabel {
                background: hsl(226, 10%, 90%);
                border-radius: 5px;
                font-size: 15px;
                padding: 15px 15px;
            }""")
        head_layout.addWidget(sectores)

        self.reg_lay.addLayout(head_layout)
        
    def sectores(self):
        sector = Sectores()
        self.reg_lay.addWidget(sector) 
           
class Main_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("9 ROOMS")
        self.setWindowIcon(QIcon("assets/Icon.png"))

        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.sidebar()
        self.contenido()
        self.setLayout(self.main_layout)

    def sidebar(self):
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(200)
        
        sidebar.setStyleSheet("""
            #sidebar {
                background: hsl(226, 100%, 67%);
            }""")

        side_lay = QVBoxLayout()
        side_lay.setContentsMargins(0, 0, 0, 0)

        logo = QLabel() 
        logo.setPixmap(QPixmap("assets/Logo.png"))
        logo.setScaledContents(True)
        logo.setFixedSize(200, 160)
        side_lay.addWidget(logo)

        opciones = ["Registro", "Búsqueda", "Reporte", "Modificaciones", "Eliminar"]
        for opcion in opciones:
            btn = QPushButton(opcion)
            btn.clicked.connect(self.cambiar_indice)
            btn.setObjectName("btn")
            btn.setStyleSheet("""
                #btn{
                    background-color: transparent;
                    color: white;
                    padding: 15px 20px;
                    font-size: 15px;
                    border-radius: 15px;
                }
                #btn:hover {
                    background-color: rgba(255, 255, 255, 0.1);
                }""")
            side_lay.addWidget(btn)

        sidebar.setLayout(side_lay)
        side_lay.addStretch()
        self.main_layout.addWidget(sidebar)

    def contenido(self):
        self.indice = QStackedWidget()

        self.indice.addWidget(Registro()) 
        self.indice.addWidget(Busqueda())
        self.indice.addWidget(Reporte())
        self.indice.addWidget(Modificaciones())
        self.indice.addWidget(Eliminar())

        self.main_layout.addWidget(self.indice)

    def cambiar_indice(self):
        btn = self.sender().text()
        match btn:
            case "Registro": self.indice.setCurrentIndex(0)
            case "Búsqueda": self.indice.setCurrentIndex(1)
            case "Reporte": self.indice.setCurrentIndex(2)
            case "Modificaciones": self.indice.setCurrentIndex(3)
            case "Eliminar": self.indice.setCurrentIndex(4)

#==============================================================================
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
    def __init__(self, path):
        self.path = path
        self.habitaciones = {}
        
    def registro(self, hab, nombre, ciudad, dias, forma, can=1):
            if hab in self.habitaciones: 
                raise ValueError("Habitación Ocupada")
            
            self.habitaciones[hab] = cliente(hab, nombre, ciudad, dias, forma, can)
            guardar(self.habitaciones, self.path)

    def busqueda(self, hab):
         if hab in self.habitaciones: return self.habitaciones[hab].cinfo()
         else: return "Habitación vacía"

    def tabla(self):
        return ["Ocupado" if i in self.habitaciones else "Vacío" for i in range(1,10)]
              
    def mod(self, hab, dias_n):
        if hab not in self.habitaciones: return "Habitación vacía"
        self.habitaciones[hab].dias = dias_n
        guardar(self.habitaciones, self.path)

    def eliminar(self, hab):
        if hab not in self.habitaciones: return "Habitación vacía" 
        self.habitaciones.pop(hab)
        guardar(self.habitaciones, self.path)
                                  
def guardar(datos, path):
     with open(path,"w") as f:
        print("-"*140, file = f)
        print(f"{"HABITACION":^20}{"NOMBRE":^20}{"CIUDAD":^20}{"ESTANCIA":^20}{"NUM.P":^20}{"TOTAL":^20}{"PAGO":^20}", file = f)
        print("-"*140, file = f)
        for hab, cliente in datos.items(): 
            print(f"{hab:^20}{cliente.nombre:^20}{cliente.ciudad:^20}{cliente.dias:^20}{cliente.can:^20}{cliente.total:^20}{cliente.forma:^20}", file = f)
        print("-"*140, file = f)
        texto = f"INGRESOS TOTALES: {sum(x.total for x in datos.values())}"
        print(f"{texto:^140}", file=f)
        print("-"*140, file = f)

if __name__ == "__main__":
    path = "informe.txt"      
    Hotel = hotel(path)
    App = QApplication([])
    MainWindow = Main_Window()
    MainWindow.show()
    App.exec_()