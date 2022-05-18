class Cuenta:
    
  def __init__(self, titular, cantidad):
       self.titular=titular
       self.cantidad=cantidad    

  def mostrar(self):
    print("Los datos de la cuenta son, Titular: ", self.titular, "y dispone de: $", self.cantidad)

  def ingresar(self):
    print("El saldo de tu cuenta es de: ", self.cantidad + 4500)

  def retirar(self):
    print("El saldo de tu cuenta es de: ", self.cantidad - 5000)
  
cuenta1=Cuenta("Pedro Ramirez", 4000)
cuenta1.mostrar()
cuenta1.ingresar()
cuenta1.retirar()

print("Mi nombrer es Mariano")