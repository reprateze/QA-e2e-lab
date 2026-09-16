from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

class BasePage:
        
    CART_PRECO = ".cart_price"
    CART_QUANTIDADE = ".cart_quantity"
    CART_TOTAL = ".cart_total_price"

    def __init__(self, page):
        self.page = page

    def goto(self, path: str = "/"):
        self.page.goto(path)

    def title(self) -> str:
        return self.page.title()

    def fill(self, selector: str, texto: str):
        self.page.fill(selector, texto)

    def select(self, seletor: str, texto: str):
        self.page.select_option(seletor, texto)

    def click(self, seletor: str):
        self.page.click(seletor)

    def pagina_visivel(self, padrao_url: str) -> bool:
        try:
            self.page.wait_for_url(f"**{padrao_url}**", timeout=5000)
            return True
        except PlaywrightTimeoutError:
            return False
        
    def _extrair_valor(self, texto: str) -> float:
        texto_limpo = texto.replace("Rs.", "").strip()
        return float(texto_limpo)

    def totais_batem(self) -> bool:
        linhas = self.page.locator("#cart_info_table tbody tr")
    
        for i in range(linhas.count()):
            linha = linhas.nth(i)
        
            preco_texto = linha.locator(self.CART_PRECO).inner_text()
            quantidade_texto = linha.locator(self.CART_QUANTIDADE).inner_text()
            total_texto = linha.locator(self.CART_TOTAL).inner_text()

            preco = self._extrair_valor(preco_texto)
            quan = int(quantidade_texto)
            total_exibido = self._extrair_valor(total_texto)

            if preco * quan != total_exibido:
                return False

        return True
        
