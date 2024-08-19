class EntityAPI:
    def __init__(self, api):
        self.api = api

    def get(self, **kwargs):
        return self.api.get(**kwargs)

    # def  post(self, **kwargs):
    #     return self.api. post(**kwargs)

    # def  put(self, **kwargs):
    #     return self.api. put(**kwargs)

    # def  delete(self, **kwargs):
    #     return self.api. delete(**kwargs)
