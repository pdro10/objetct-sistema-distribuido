import sys
from omniORB import CORBA
import CosNaming
import Example

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

obj = orb.resolve_initial_references("NameService")
rootContext = obj._narrow(CosNaming.NamingContext)

name = [CosNaming.NameComponent("SomaService", "")]
obj = rootContext.resolve(name)

soma = obj._narrow(Example.Soma)

print("=== Cliente de Soma ===")
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

resultado = soma.calcularSoma(a, b)
print(f"Resultado vindo do servidor: {resultado}")
