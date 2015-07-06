from AuthHandler import AuthHandler

import json


class BaseHandler(AuthHandler):

    def serve_json(self, dict):
        self.response.write(json.dumps(dict))
