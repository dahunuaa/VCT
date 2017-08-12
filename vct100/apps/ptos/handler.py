# -*- coding:utf-8 -*-
from vct100.apps.base.handler import TokenHandler,SingleStandardHanler,MultiStandardHandler
from vct100.libs.oauthlib import get_provider

class PtosListHandler(MultiStandardHandler,TokenHandler):
    _model = "ptos.PtosModel"
    enable_methods = ["post","get"]
    private = False

class PtosHandler(SingleStandardHanler,TokenHandler):
    _model = "ptos.PtosModel"
    enable_methods = ["get","put","delete"]

class AddresultHandler(SingleStandardHanler,TokenHandler):
    _model = "ptos.PtosModel"
    enable_methods = ["put"]
    def put(self):
        result = self.get_argument("result",None)
        ptos_id = self.get_argument("ptos_id", None)
        res = self.model.add_result(result,ptos_id)
        self.result["data"]=res
        self.finish(self.result)

handlers =[
    (r"",PtosListHandler,get_provider("ptos")),
    (r"/add_result",AddresultHandler,get_provider("ptos")),
    (r"/(.*)",PtosHandler,get_provider("ptos"))
]