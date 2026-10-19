from pages.base_page import BasePage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

class ProductPage(BasePage):

    SEARCH_INPUT = "#search_product"
    SUBMIT_SEARCH = "#submit_search"
    PRODUCT_NAMES = ".productinfo p"
    PRODUCT_LINK = "a[href='/product_details/2']"
    ADD_PRODUTO_DETAILS = ".btn.btn-default.cart"
    QUANTITY_INPUT = "#quantity"
    NAME_INPUT = "#name"
    EMAIL_INPUT = "#email"    
    REVIEW_INPUT = "#review"
    REVIEW_BUTTON = "#button-review"
    FECHAR_MODAL = "button.close-modal"

      
    def adicionar_produto_ao_carrinho(self, nome_produto: str):
        produto = self.page.locator(".productinfo").filter(has_text=nome_produto)
        produto.hover()
        produto.locator(".add-to-cart").click()

    def produto_adicionado_sucesso(self) -> bool:
        locator = self.page.get_by_text("Your product has been added to cart.")
        try:
            locator.wait_for(state="visible", timeout=5000)
            return True
        except PlaywrightTimeoutError:
         return False

    def pesquisar(self, termo: str):
        self.fill(self.SEARCH_INPUT, termo)
        self.click(self.SUBMIT_SEARCH)

    def get_produtos_nome(self):
        self.page.locator(self.PRODUCT_NAMES).first.wait_for(state="visible")
        return self.page.locator(self.PRODUCT_NAMES).all_text_contents()

    def acessar_detalhes_produto(self, produto_id: int):
        self.page.locator(f"a[href='/product_details/{produto_id}']").click()

    def pagina_detalhes_adicionar_produto(self):
        self.click(self.ADD_PRODUTO_DETAILS)

    def altera_quantidade_produtos(self, quantidade):
        self.fill(self.QUANTITY_INPUT, str(quantidade))

    def obter_quantidade(self) -> str:
        return self.page.input_value(self.QUANTITY_INPUT) 

    def preencher_review(self, nome: str, email: str, texto: str):
        self.fill(self.NAME_INPUT, nome)
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.REVIEW_INPUT, texto)
        self.click(self.REVIEW_BUTTON)

    def review_enviada_com_sucesso(self, timeout: int = 10000) -> bool:
        try:
            self.page.get_by_text("Thank you for your review.").wait_for(state="visible", timeout=timeout)
            return True
        except TimeoutError:
            return False

        
    def fechar_modal_adicionado(self):
        self.click(self.FECHAR_MODAL)
    

        
