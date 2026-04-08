import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_item_checkout(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.backpack_add.click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test='firstName']").fill("João")
    page.locator("[data-test='lastName']").fill("Silva")
    page.locator("[data-test='postalCode']").fill("1000-001")
    page.locator("[data-test=\"continue\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

def test_error_information(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.backpack_add.click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"continue\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_have_text("Error: First Name is required")
