# -*- coding:utf-8 -*-

from vct100.apps.base.handler import TokenHandler,MultiStandardHandler,SingleStandardHanler
from vct100.libs.oauthlib import get_provider

class PtosAddListHandler(MultiStandardHandler,TokenHandler):
    _model = "ptosadd.PtosaddModel"
    enable_methods = ["post","get"]
    private = False

class PtosAddHandler(SingleStandardHanler,TokenHandler):
    _model = "ptosadd.PtosaddModel"
    enable_methods = ["get","put","delete"]

handlers = [
    (r"",PtosAddListHandler,get_provider("ptosadd")),
    (r"/(.*)",PtosAddHandler,get_provider("ptosadd"))
]