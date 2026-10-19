from pages.base_page import BasePage

class CartPage(BasePage):

    CART_PRODUCT_NAMES = ".cart_description h4"
    REMOVER_BUTTON = ".cart_quantity_delete"
    CARRINHO_VAZIO = "#empty_cart"
    CART_PRECO = ".cart_price"
    CART_QUANTIDADE = ".cart_quantity button"
    CART_TOTAL = ".cart_total"
    IR_PARA_CHECKOUT = ".check_out"

    def get_produtos_no_carrinho(self) -> list[str]:
        return self.page.locator(self.CART_PRODUCT_NAMES).all_text_contents()
    
    def remover_todos_produtos(self):
        import time
        while self.page.locator(self.REMOVER_BUTTON).count() > 0:
            self.page.locator(self.REMOVER_BUTTON).first.click()
            time.sleep(2)

    def get_carrinho_vazio(self) -> bool:
        return self.page.locator(self.CARRINHO_VAZIO).is_visible()

    def ir_para_checkout(self):
        self.click(self.IR_PARA_CHECKOUT)
