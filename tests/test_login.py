import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_login_com_credenciais_corretas(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_username_errado(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("wrong_user", "secret_sauce")
    # ← apaga o page.get_by_role("button"...) que estava aqui
    expect(page.locator(".error-message-container")).to_be_visible()

def test_campos_vazios(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("", "")
    # ← apaga o page.get_by_role("button"...) que estava aqui
    expect(page.locator(".error-message-container")).to_be_visible()

def test_login_utilizador_bloqueado(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("locked_out_user", "secret_sauce")
    # ← apaga o page.get_by_role("button"...) que estava aqui
    # ← muda login_page para page
    expect(page.locator(".error-message-container")).to_be_visible()

def test_logout(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    # ← apaga o page.get_by_role("button", name="Login") que estava aqui
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test='logout-sidebar-link']").click()
    expect(page).to_have_url("https://www.saucedemo.com/")