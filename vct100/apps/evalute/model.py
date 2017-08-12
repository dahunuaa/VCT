# -*- coding:utf-8 -*-
import vct100.apps.base.model as model
from vct100.libs.datatypelib import *

class EvaluteModle(model.StandCURDModel):
    _coll_name="evalute"
    _columns=[
        ("buss_id",StrDT(required=True)),
        ("rank",StrDT(required=True)),
        ("comment",StrDT(required=True)),
        ("evalute_name",StrDT(required=True))
    ]