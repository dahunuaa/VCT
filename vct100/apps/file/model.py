# -*- coding:utf-8 -*-
import vct100.apps.base.model as model
from vct100.libs.datatypelib import *
import os
from vct100.libs.utils import *

class FileModel(model.StandCURDModel):
    _coll_name = "file"
    _columns = [
        ("file_name",StrDT()),
        ("file_path",StrDT())

    ]



