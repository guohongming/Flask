#!usr/bin/env python

from urllib import parse, request
import hashlib
import datetime

# from Crypto.Cipher import AES    #此模块非python自带模块，如需使用加密短信，请开发者自行安装调试，

'''
美圣融云短信管理平台API开发Python示例
详细接口说明文档请参考《美圣融云平台接口文档.doc》
'''


class RCSCLOUDAPI:
    '美圣融云短信接口，官网：http://www.rcscloud.cn'

    # 短信帐号
    __ACCOUNT_SID = "ZH000000569"

    # 通讯认证Key
    __ACCOUNT_APIKEY = "9aa6e59c-862f-46a2-bf71-07849868b929"
    __SERVER_IP = "api.rcscloud.cn"
    __SERVER_PORT = "8030"

    # ------------------------以下是接口的封装------------------------------


    # 获取账号信息
    @classmethod
    def getAccount(self):
        # 签名摘要
        sign = self.md5Digest('%s%s' % (self.__ACCOUNT_SID, self.__ACCOUNT_APIKEY))
        # 请求url
        url = "http://%s:%s/rcsapi/rest/user/get.json" % (self.__SERVER_IP, self.__SERVER_PORT)
        paras = {"sid": self.__ACCOUNT_SID, "sign": sign}
        # 采用get方式
        return self.HttpGet(url, paras)

    '''
    发送模板短信
    '''

    @classmethod
    def sendTplSms(self, templateId, mobile, content, extno=""):
        # 请求头部设置认证信息
        signtext = '%s%s%s%s%s' % (self.__ACCOUNT_SID, self.__ACCOUNT_APIKEY, templateId, mobile, content)
        sign = self.md5Digest(signtext)
        # 请求参数
        paras = {"sid": self.__ACCOUNT_SID, "sign": sign, "tplid": templateId, "mobile": mobile, "content": content,
                 "extno": extno}
        # 构建请求URL，所有url都必须包含sign、sid参数
        url = "http://%s:%s/rcsapi/rest/sms/sendtplsms.json" % (self.__SERVER_IP, self.__SERVER_PORT);
        return self.HttpPost(url, paras)

        # ----------------------------以下是公共方法---------------------------------

    # post请求
    @staticmethod
    def HttpPost(url, paras):
        # json串数据使用#
        # postdata = json.dumps(paras).encode(encoding='utf-8')
        # print(postdata)
        # 普通数据使用
        postdata2 = parse.urlencode(paras).encode(encoding='utf-8')
        header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                       "Content-Type": "application/json"}
        req = request.Request(url=url, data=postdata2)  # ,headers=header_dict
        res = request.urlopen(req)
        text = res.read()
        # print(text.decode("utf8"))
        return text

    # get请求
    @staticmethod
    def HttpGet(url, paras):
        textmod = parse.urlencode(paras)
        req = request.Request(url='%s%s%s' % (url, '?', textmod))
        res = request.urlopen(req)
        res = res.read()
        return res

    @staticmethod
    def md5Digest(str):
        m = hashlib.md5()
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def currentTimestamp():
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S')
