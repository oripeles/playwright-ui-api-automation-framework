from playwright.sync_api import APIResponse
from api.clients.base_api_client import BaseApiClient


class BrandsClient(BaseApiClient):

    def get_all_brands(self) -> APIResponse:
        return self.get("/api/brandsList")

    def post_brands_list_not_supported(self) -> APIResponse:
        return self.post("/api/brandsList")

    def put_brands_list_not_supported(self) -> APIResponse:
        return self.put("/api/brandsList")
