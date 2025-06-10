import json

class TypeUserTelaController:

    def __init__(self, admin_frame, default_frame):
        self.admin_frame = admin_frame
        self.default_frame = default_frame
    
    def handle(self):

        with open("cache.json", "r", encoding="utf-8") as cache:
            dados = json.load(cache)

        if dados['TYPE_USER'] == True:

            self.admin_frame()
        
        else:
            self.default_frame()