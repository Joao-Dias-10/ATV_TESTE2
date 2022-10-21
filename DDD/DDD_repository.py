from DDD import Destino


class ddd_repository:
    destino_lista: Destino = []

    def __init__(self) -> None:
        pass

    def checa_se_destino_existe(self, destino: Destino) -> bool:
        for item in self.destino_lista:
            if destino.ddd == item.ddd and destino.destino == item.destino:
                return True
        return False

    def adicionar_destino(self, destino: Destino) -> bool:
        if not self.checa_se_destino_existe(destino):
            self.destino_lista.append(destino)
            return True
        return False

    def obter_destino_pelo_ddd(self, ddd: int) -> str:
        for item in self.destino_lista:
            if item.ddd == ddd:
                return item.destino
        return "DDD informado não cadastrado"

    def __str__(self) -> str:
        formatText = "{0:<5} {1:<0}\n"
        menu = formatText.format("DDD:", "Localidade:")

        for item in self.destino_lista:
            menu += formatText.format(item.ddd, item.destino)

        return menu
