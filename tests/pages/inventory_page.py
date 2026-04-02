# pages/inventory_page.py
from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        # localizadores da página de produtos
        self.backpack_add = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.backpack_remove = page.locator("[data-test='remove-sauce-labs-backpack']")
        self.backpack_link = page.locator("[data-test='item-4-title-link']")

    def add_backpack_to_cart(self):
        self.backpack_add.click()