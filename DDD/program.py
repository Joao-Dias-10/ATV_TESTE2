from DDD import Destino
from DDD_repository import ddd_repository
from interface_user import interface_user


repository = ddd_repository()
repository.adicionar_destino(Destino(61, "Brasilia"))
repository.adicionar_destino(Destino(71, "Salvador"))
repository.adicionar_destino(Destino(11, "Sao Paulo"))
repository.adicionar_destino(Destino(21, "Rio de Janeiro"))
repository.adicionar_destino(Destino(32, "Juiz de Fora"))
repository.adicionar_destino(Destino(19, "Campinas"))
repository.adicionar_destino(Destino(27, "Vitoria"))
repository.adicionar_destino(Destino(31, "Belo Horizonte"))

print(repository)

interface = interface_user(repository)

print(interface.saida_usuario())
