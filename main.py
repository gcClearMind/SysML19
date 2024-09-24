# -*- coding = utf-8 -*-
from py2neo import Graph, Node, Relationship
from xml.dom.minidom import parse
import xml.dom.minidom
import configparser

# 参数中读取不需要读的信息
CONFIG_FILE = 'config.ini'
config = configparser.ConfigParser()
config.read(CONFIG_FILE)

# 节点、关系列表
NodeList = []
RelationList = []
NodeDict = {}
U2Sdict = {}
isNode = {}






if __name__ == '__main__':
    print("123")