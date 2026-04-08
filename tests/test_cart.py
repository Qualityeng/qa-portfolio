import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_item_cart(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.backpack_add.click()
    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")
    
def test_remove_item_cart(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.backpack_add.click()   
    inventory.backpack_remove.click()
    expect(page.locator("[data-test='shopping-cart-badge']")).not_to_be_visible()

def test_add_various_items(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.backpack_add.click()
    inventory.bike_light_add.click() 
    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("2")