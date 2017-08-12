# -*- coding:utf-8 -*-
from vct100.apps.base.handler import TokenHandler,MultiStandardHandler,SingleStandardHanler
from vct100.libs.oauthlib import get_provider

class NoticereadListHandler(TokenHandler,MultiStandardHandler):
    _model = "noticeread.NoticereadModel"
    enable_methods = ['get']
    private = False



class NoticeHandler(MultiStandardHandler,TokenHandler):
    _model = "noticeread.NoticereadModel"
    enable_methods = ['put']

    def _put(self):
        user_id = self.get_argument("user_id")
        msg_id = self.get_argument("msg_id")
        res = self.model.minus(user_id,msg_id)
        self.result['data']=res


handlers = [
    (r"/minus",NoticeHandler,get_provider("noticeread")),#此处用put但是 不是直接附id，所以继承MultiStandardHandler
    (r"",NoticereadListHandler,get_provider("noticeread")),
    # (r"/(.*)",NoticeHandler,get_provider("noticeread"))
]
