from DDD import Destino
from DDD_repository import ddd_repository


def test_checa_se_destino_existe():
    # Arrange
    destino1 = Destino(75, "Feira de Santana")
    destino2 = Destino(69, "Uberlandia")
    repository = ddd_repository()
    repository.adicionar_destino(destino1)

    # Act
    ddd_existe = repository.checa_se_destino_existe(destino1)
    ddd_nao_existe = repository.checa_se_destino_existe(destino2)

    # Assert
    assert ddd_existe == True
    assert ddd_nao_existe == False


def test_adicionar_destino():
    # Arrange
    add_destino = Destino(77, "Cogulandia")
    repository = ddd_repository()

    # Act
    ddd_existe = repository.adicionar_destino(add_destino)
    ddd_nao_existe = repository.adicionar_destino(add_destino)
    # Assert
    assert ddd_existe == True
    assert ddd_nao_existe == False


def test_obter_destino_pelo_ddd():
    # Arrange
    retorna_destino = Destino(77, "Cogulandia")
    repository = ddd_repository()
    repository.adicionar_destino(retorna_destino)

    # Act
    ddd_existe = repository.obter_destino_pelo_ddd(retorna_destino.ddd)
    ddd_nao_existe = repository.obter_destino_pelo_ddd(2)
    # Assert
    assert ddd_existe == "Cogulandia"
    assert ddd_nao_existe == "DDD informado não cadastrado"
