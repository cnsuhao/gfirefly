#coding:utf8
'''
Created on 2013-8-2

@author: lan (www.9miao.com)
'''
from gfirefly.utils.singleton import Singleton

class GlobalObject:
    
    __metaclass__ = Singleton
    
    def __init__(self):
        self.netfactory = None#net前端
        self.root = None#分布式root节点
        self.remote = {}#remote节点
        self.db = None
        self.stophandler = None
        self.webroot = None
        self.masterremote = None
        self.reloadmodule = None
        self.remote_connect = None
        self.json_config = {}
        self.remote_map = {}
        
    def config(self,netfactory=None,root = None,remote=None,db=None):
        self.netfactory = netfactory
        self.root = root
        self.remote = remote
        self.db = db
        
def masterserviceHandle(target):
    """
    """
    GlobalObject().masterremote._reference._service.mapTarget(target)
        
def netserviceHandle(target):
    """
    """
    GlobalObject().netfactory.service.mapTarget(target)
        
def rootserviceHandle(target):
    """
    """
    GlobalObject().root.service.mapTarget(target)
    
class webserviceHandle:
    """这是一个修饰符对象
    """
    
    def __init__(self,url,**kw):
        """
        @param url: str http 访问的路径
        """
        self._url = url
        self.kw = kw
        
    def __call__(self,cls):
        """
        """
        if self._url:
            child_name = self._url
        else:
            child_name = cls.__name__
        return GlobalObject().webroot.route(child_name,**self.kw)(cls)
    

    
class remoteserviceHandle:
    """
    """
    def __init__(self,remotename):
        """
        """
        self.remotename = remotename
        
    def __call__(self,target):
        """
        """
        GlobalObject().remote[self.remotename]._reference._service.mapTarget(target)
        
