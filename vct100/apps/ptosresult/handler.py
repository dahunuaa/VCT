# -*- coding:utf-8 -*-

from vct100.apps.base.handler import TokenHandler,MultiStandardHandler,SingleStandardHanler
from vct100.libs.oauthlib import get_provider

class PtosResultListHandler(MultiStandardHandler,TokenHandler):
    _model = "ptosresult.PtosresultModel"
    enable_methods = ["post","get"]
    private = False

class PtosResultHandler(SingleStandardHanler,TokenHandler):
    _model = "ptosresult.PtosresultModel"
    enable_methods = ["get","put","delete"]

handlers = [
    (r"",PtosResultListHandler,get_provider("ptosresult")),
    (r"/(.*)",PtosResultHandler,get_provider("ptosresult"))
]