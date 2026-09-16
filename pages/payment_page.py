from pages.base_page import BasePage
import re
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

class  PaymentPage(BasePage):

    INPUT_NOMECARTAO = '[data-qa="name-on-card"]'
    INPUT_NUMEROCARTAO = '[data-qa="card-number"]'
    INPUT_CVC = '[data-qa="cvc"]'
    INPUT_MONTH =  '[data-qa="expiry-month"]'
    INPUT_YEAR =  '[data-qa="expiry-year"]'
    BUTTON_PAY = '[data-qa="pay-button"]'
    PEDIDO_CONCLUIDO = '[data-qa="order-placed"]'


    def preencher_dados_cartao(self, nome, numero, cvc, mes, ano):
        # Usa os seletores para preencher tudo
        self.fill(self.INPUT_NOMECARTAO, nome)
        self.fill(self.INPUT_NUMEROCARTAO, numero)
        self.fill(self.INPUT_CVC, cvc)
        self.fill(self.INPUT_MONTH, mes)
        self.fill(self.INPUT_YEAR, ano)
        
    def confirmar_pagamento(self):
        self.page.locator(self.BUTTON_PAY).click()
        try:
            self.page.wait_for_url(re.compile(r".*payment_done.*"), timeout=15000)
        except PlaywrightTimeoutError:
            pass  

    def pedido_concluido_visivel(self, timeout: int = 5000) -> bool:
        return self.page.wait_for_locator(self.PEDIDO_CONCLUIDO, timeout=timeout).is_visible()
