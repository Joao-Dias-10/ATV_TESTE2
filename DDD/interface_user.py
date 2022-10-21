from DDD_repository import ddd_repository
from DDD import Destino


class interface_user:
    def __init__(self, ddd_repository: ddd_repository) -> None:
        self.ddd_repository = ddd_repository

    def exibir_destinos(self) -> list:
        return self.ddd_repository

    def saida_usuario(self) -> str:
        ddd = int(input("Diga o ddd: "))
        destino = self.ddd_repository.obter_destino_pelo_ddd(ddd)
        return f"Destino: {destino}"
