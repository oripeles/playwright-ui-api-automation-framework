from playwright.sync_api import APIResponse
from api.clients.base_api_client import BaseApiClient


class ProductsClient(BaseApiClient):
    def get_all_products(self) -> APIResponse:
        return self.get("/api/productsList")

    def post_products_list(self) -> APIResponse:
        return self.post("/api/productsList")

    def search_product(self, search_term: str) -> APIResponse:
        return self.post(
            "/api/searchProduct",
            form={"search_product": search_term},
        )

    def search_product_without_param(self) -> APIResponse:
        return self.post("/api/searchProduct")
