from playwright.sync_api import APIResponse
from api.clients.base_api_client import BaseApiClient

class AuthClient(BaseApiClient):
    def verify_login(self, email: str, password: str) -> APIResponse:
        return self.post("/api/verifyLogin", form={"email": email, "password": password})

    def verify_login_without_email(self, password: str) -> APIResponse:
        return self.post("/api/verifyLogin", form={"password": password})

    def delete_verify_login(self) -> APIResponse:
        return self.delete("/api/verifyLogin")

    def create_account(self, payload: dict) -> APIResponse:
        return self.post("/api/createAccount", form=payload)

    def delete_account(self, email: str, password: str) -> APIResponse:
        return self.delete("/api/deleteAccount", form={"email": email, "password": password})

    def get_user_detail_by_email(self, email: str) -> APIResponse:
        return self.get("/api/getUserDetailByEmail", params={"email": email})
