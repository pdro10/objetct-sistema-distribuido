import sys
import omniORB
import CosNaming
from omniORB import CORBA
import Example__POA

class Soma_i(Example__POA.Soma):
    def calcularSoma(self, a, b):
        print(f"Recebido pedido calcularSoma({a}, {b})")
        return a + b

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)


poa = orb.resolve_initial_references("RootPOA")
poa_manager = poa._get_the_POAManager()
poa_manager.activate()

obj = orb.resolve_initial_references("NameService")
rootContext = obj._narrow(CosNaming.NamingContext)

if rootContext is None:
    print("Erro: NameService não está rodando")
    sys.exit(1)

soma_obj = Soma_i()
ref = soma_obj._this()

name = [CosNaming.NameComponent("SomaService", "")]
rootContext.rebind(name, ref)

print("Servidor de Soma iniciado e AGUARDANDO requisições...")

orb.run()