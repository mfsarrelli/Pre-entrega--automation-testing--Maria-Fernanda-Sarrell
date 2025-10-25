import pytest

from selenium.webdriver.common.by import By
import sys ##sirve para encontrar archivos dentro de mi root
import os ##transforma rutas relativas cleen absolutas


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.helpers import login_saucedemo, get_driver





@pytest.fixture(scope='session') ##mantiene la sesion del navegador iniciada para que se ejecuten todos los test
def driver():
    # configuracion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()



def test_login(driver):

    login_saucedemo(driver)
    assert "/inventory.html" in driver.current_url
    titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == 'Products'

    #logueo de usuario 
    #click boton de login
    #assert la palabra "inventory" dentro de la URL y el titulo "Swag Labs"


def test_catalogo(driver):
    login_saucedemo (driver)

    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(productos)>0

##def test_catalogo():
    #logueo de usuario
    #click boton de login
    #assert si existen productos visibles en la pagina (lenght()>0)
    #verificar elementos importantes de la pagina

def test_carrito(driver):

    login_saucedemo (driver)
    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    total_productos = len(productos)

    if total_productos >= 2:
        productos[0].find_element(By.TAG_NAME, 'button').click()
        productos[1].find_element(By.TAG_NAME, 'button').click()
        
        badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        assert badge == "2"


    #logueo de usuario
    #click boton de login
    #llevarme a la pagina de carrito de compras
    #inspeccionar elemento carrito, con su class name descender al hijo y buscar el span que tiene el numero de elementos
    #comprobar que el carrito agrego el producto