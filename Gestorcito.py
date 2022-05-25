
#Se define la clase usuario, con respectivo metodo constructor.
class Usuario():
    
    print("\n")
    print("   ==================================")
    print("         Bienvenido a GestorCito     ")
    print("   ==================================")
    print("\n")
    
    def __init__(self):
        valido = True  
        while valido == True:
            try:
                usuario = input("\nIngrese su usuario : ")
                contraseña= input("Ingrese su contraseña : ")
                cargo = input("Ingrese tipo de usuario : ")
                break
            except Exception:
                print("Algo salio mal, por favor intente nuevamente")
        self.usuario = usuario.lower()
        self.contraseña = contraseña.lower()
        self.cargo = cargo.lower()
        
    def get_tipo(self):
        return self.cargo
    
    def get_usuario(self):
        print("Usuario : ",self.usuario)
        
#Se define la clase Menu, con sus submenues y se hereda a la clase Usuario para poder usar sus atributos.
class Menu(Usuario):
    
    def __init__(self):
        super().__init__() #se hereda a la clase Usuario para poder usar sus atributos con super.
    

    def menuSocio(self):
        print("\n")
        print("   ==================================")
        print("          Bienvenido Socio : ",self.usuario)
        print("   ==================================")
        print("\n")
        print("1 - Consultar stock")
        print("2 - Modificar stock")
        print("3 - Ver Pedidos")
        print("4 - Modificar Pedidos")
        print("5 - Ver Clientes")
        print("6 - Modificar Clientes")
        print("7 - Ver Nomina Empleados")
        print("8 - Modificar Nomina de Empleados")
        print("9 - Limpiar Pantalla")
        print("10 - Salir")
  
        
        
        valido = True  
        while valido == True:
            try:
                opcion = int(input("\nIngrese su opcion: "))
                break
            except ValueError:
                print("Por favor ingrese solo numeros,")
        
        
        if opcion <= 9:
            exit("**** Sitio en mantenimiento, disculpe las molestias. ****")
        elif opcion == 10:
            exit("Gracias por usar GestorCito.")
    
            
        
               
        
        

    
    def menuManager(self):
        print("\n")
        print("   ==================================")
        print("          Bienvenido Manager     ",self.usuario)
        print("   ==================================")
        print("\n")
        print("1 - Consultar stock")
        print("2 - Modificar stock")
        print("3 - Ver Pedidos")
        print("4 - Modificar Pedidos")
        print("5 - Ver Clientes")
        print("6 - Modificar Clientes")
        print("7 - Limpiar Pantalla")
        print("8 - Salir")
        
        valido = True  
        while valido == True:
            try:
                opcion = int(input("\nIngrese su opcion: "))
                break
            except ValueError:
                print("Por favor ingrese solo numeros,")
        
        
        if opcion <= 7:
            exit("**** Sitio en mantenimiento, disculpe las molestias. ****")
        elif opcion == 8:
            exit("Gracias por usar GestorCito.")

    def menuVentas(self):
        print("\n")
        print("   ==================================")
        print("          Bienvenido Ventas :    ",self.usuario)
        print("   ==================================")
        print("\n")
        print("1 - Consultar stock")
        print("2 - Modificar stock")
        print("3 - Ver Pedidos")
        print("4 - Modificar Pedidos")
        print("5 - Ver Clientes")
        print("6 - Limpiar Pantalla")
        print("7 - Salir")
        
        valido = True  
        while valido == True:
            try:
                opcion = int(input("\nIngrese su opcion: "))
                break
            except ValueError:
                print("Por favor ingrese solo numeros,")
        
        
        if opcion <= 6:
            exit("**** Sitio en mantenimiento, disculpe las molestias. ****")
        elif opcion == 7:
            exit("Gracias por usar GestorCito.")

    def menuAdministrativo(self):
        print("\n")
        print("   ==================================")
        print("         Bienvenido Administrativo :   ",self.usuario)
        print("   ==================================")
        print("\n")
        print("1 - Consultar stock")
        print("2 - Modificar stock")
        print("3 - Ver Pedidos")
        print("4 - Limpiar Pantalla")
        print("5 - Atras")
        
        valido = True  
        while valido == True:
            try:
                opcion = int(input("\nIngrese su opcion: "))
                break
            except ValueError:
                print("Por favor ingrese solo numeros,")
        
        
        if opcion <= 4:
            exit("**** Sitio en mantenimiento, disculpe las molestias. ****")
        elif opcion == 5:
            exit("Gracias por usar GestorCito.")

    def menuSoporte(self):
        print("\n")
        print("   ==================================")
        print("         Bienvenido Soporte  :  ",self.usuario)
        print("   ==================================")
        print("\n")
        print("1 - Modificar Menu Socio")         
        print("2 - Modificar Menu Manager")
        print("3 - Modificar Menu Ventas")
        print("4 - Modificar Menu Administrativo")
        print("5 - Limpiar Pantalla")
        print("6 - Atras")
        
        valido = True  
        while valido == True:
            try:
                opcion = int(input("\nIngrese su opcion: "))
                break
            except ValueError:
                print("Por favor ingrese solo numeros,")
        
        
        if opcion <= 5:
            exit("**** Sitio en mantenimiento, disculpe las molestias. ****")
        elif opcion == 6:
            exit("Gracias por usar GestorCito.")
            
        
    def limpioPantalla(self):
        sisOper = os.name
        if sisOper == "posix":   # si fuera UNIX, mac para Apple, java para maquina virtual Java
            os.system("clear")
        elif sisOper == "ce" or sisOper == "nt" or sisOper == "dos":
                os.system("cls")

    def mostrarMenu(self):
        

        

            
        if self.cargo == "socio":
            self.menuSocio()
            
        elif self.cargo == "manager":
            self.menuManager()
            
        elif self.cargo == "ventas":
            self.menuVentas()
            
        elif self.cargo == "administrativo":
            self.menuAdministrativo()
            
        elif self.cargo == "soporte":
            self.menuSoporte()
        
        elif self.cargo != "socio" or "administrativo" or "manager" or "ventas" or "soporte":
            print("Por favor ingrese un tipo de usuario correcto (socio,manager,ventas,administrativo y soporte)")
            cla = Menu()
            cla.mostrarMenu()
        else:
            print("Ingrese un tipo de usuario valido, por favor intente nuevamente o comuniquese con Mesa de ayuda.")
        
            
#Se instancio la clase
cla = Menu()
cla.mostrarMenu()



    
    
        
        

        
        
        
        