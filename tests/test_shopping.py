import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_complete_shopping_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    
    # 1. Login
    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    
    # 2. Agregar al carrito
    inventory_page.add_backpack_to_cart()
    
    # 3. Ir al carrito
    inventory_page.go_to_cart()
    
    # 4. Validar que el producto es el correcto
    item_name = inventory_page.get_first_item_name()
    assert item_name == "Sauce Labs Backpack"
    assert "cart.html" in driver.current_url
    
    print(f"\n ¡Flujo completo! Producto '{item_name}' validado en el carrito.")