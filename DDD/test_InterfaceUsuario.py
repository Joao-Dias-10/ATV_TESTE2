from interface_user import interface_user
from DDD import Destino
from DDD_repository import ddd_repository


def test_saida_usuario():
    # Arrange
    retorna_destino = Destino(77, "Cogulandia")
    repository = ddd_repository()
    interface = interface_user(repository)
    repository.adicionar_destino(retorna_destino)

    # Act
    ddd_existe = interface.saida_usuario()
    ddd_nao_existe = interface.saida_usuario()

    # Assert
    assert ddd_existe == "Destino: Cogulandia"
    assert ddd_nao_existe == "Destino: DDD informado não cadastrado"
