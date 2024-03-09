from requests import Session


class BaseAPI:
    def __init__(self, session: Session, route: str):
        self.session = session
        self.route = route

    def get(self, *args, **kwargs):
        response = self.session.get(*args, **kwargs)
        return response

    def post(self, *args, **kwargs):
        response = self.session.post(*args, **kwargs)
        return response

    def put(self, *args, **kwargs):
        response = self.session.put(*args, **kwargs)
        return response

    def patch(self, *args, **kwargs):
        response = self.session.patch(*args, **kwargs)
        return response

    def delete(self, *args, **kwargs):
        response = self.session.delete(*args, **kwargs)
        return response
