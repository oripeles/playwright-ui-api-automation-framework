from playwright.sync_api import APIRequestContext, APIResponse


class BaseApiClient:
    def __init__(self, request: APIRequestContext):
        self.request = request

    def get(self, path: str, **kwargs) -> APIResponse:
        return self.request.get(path, **kwargs)

    def post(self, path: str, **kwargs) -> APIResponse:
        return self.request.post(path, **kwargs)

    def put(self, path: str, **kwargs) -> APIResponse:
        return self.request.put(path, **kwargs)

    def delete(self, path: str, **kwargs) -> APIResponse:
        return self.request.delete(path, **kwargs)
