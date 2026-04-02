# test_inventory.py
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
    expect(inventory.backpack_remove).to_be_visible()

def test_open_item_link(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.backpack_link.click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory-item.html?id=4")