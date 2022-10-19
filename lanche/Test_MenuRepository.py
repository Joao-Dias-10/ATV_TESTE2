from Menu import Menu
from MenuRepository import MenuRepository
from Order import Order
from UserInterface import UserInterface


def test_set_menu_item():
    # Arrange
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    menu1 = Menu(1, "Test 1", 10)
    menu2 = Menu(2, "Test 2", 5)
    menu3 = Menu(3, "Test 3", 2)
    
    # Act
    menu_repository.set_menu_item(menu1)
    menu_repository.set_menu_item(menu2)

    # Assert
    assert len(menu_repository.menu_itens) == 2
    assert not menu3 in menu_repository.menu_itens
    assert type(menu_repository.menu_itens) == list


def test_check_if_itens_exists():
    # Arrange
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    menu1 = Menu(1, "Test 1", 10)
    order1 = Order(1, 10)
    order2 = Order(2, 10)
    
    # Act
    menu_repository.set_menu_item(menu1)
    resultOK = menu_repository.check_if_itens_exists(order1)
    resultNOK = menu_repository.check_if_itens_exists(order2)

    # Assert
    assert len(menu_repository.menu_itens) == 1
    assert resultOK == True
    assert resultNOK == False




def Pytest_get_total_price():
    # Arrange
    menu_repository = MenuRepository()
    menu = Menu(5, "Test 1", 10)
    user_interface = UserInterface(menu_repository)
    orderteste = Order(5, 50)

    # Act
    menu_repository.set_menu_item(menu)
    total_price = user_interface.get_total_price(orderteste)
    # Assert
    assert total_price == 500


def Pytest_get_user_input():
    # Arrange
    menu_repository = MenuRepository()
    user_interface = UserInterface(menu_repository)
    ordertest = Order(1, 10)

    # Act
    order = user_interface.get_user_input()

    # Assert
    assert order.code == ordertest.code
    assert order.quantity == ordertest.quantity
