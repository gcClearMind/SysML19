# -*- coding = utf-8 -*-
from py2neo import Graph, Node, Relationship

NodeList = []
RelationList = []
NodeDict = {}
U2Sdict = {}
isNode = {}


def create_graph(prods, relation, graph):
    init()
    with open(prods, 'r') as file:
        data = file.readlines()
    Id = 1
    for line in data:
        properties = line.strip().split(',')
        if not properties or properties == ['']:
            continue
        name = 'Vehicle' + str(Id)
        Id += 1
        vehicle = Node("Vehicle")
        vehicle['name'] = name
        isNode[name] = vehicle
        # 为每个属性创建节点，并连接到配置节点
        for property in properties:
            if property not in isNode.keys():
                property_node = Node("Property")
                property_node['name'] = property
                isNode[property] = property_node
            # 创建关系

            relationship = Relationship(vehicle, "HAS_PROPERTY", isNode[property])
            RelationList.append(relationship)

    with open(relation, 'r') as file:
        relationships = file.readlines()
    for line in relationships:
        parts = line.strip().split()
        if not parts or len(parts) < 3:
            continue

        node1_name = parts[0]
        if len(parts) == 3:
            rel_type = parts[1]
            node2_name = parts[2]
        else:
            rel_type = parts[1] + ' ' + parts[2]
            node2_name = parts[3]
        node1 = isNode[node1_name]
        node2 = isNode[node2_name]
        relationship = Relationship(node1, rel_type, node2)
        RelationList.append(relationship)


def test():
    for node in isNode:
        print(node)
    for relation in RelationList:
        print(relation)


# 创建节点
def createNode(graph):
    for key in isNode.keys():
        graph.create(isNode[key])
        print(isNode[key])
    for relation in RelationList:
        graph.create(relation)


# 清空图
def ClearGraph(graph):
    graph.run("MATCH(n) DETACH DELETE n")


# 初始化
def init():
    NodeList.clear()
    RelationList.clear()
    NodeDict.clear()
    U2Sdict.clear()
    isNode.clear()


def creat():
    #  NEO4J链接
    # 本地
    graph = Graph('bolt://localhost:7687', auth=('neo4j', '12345678'))
    # 服务器
    # graph = Graph('bolt://120.26.15.210:7687', auth=('neo4j', '123456'))
    #
    ClearGraph(graph)
    create_graph("model/Vehicle.prods", "model/vehicle-relation.txt", graph)
    createNode(graph)
    # test()


if __name__ == '__main__':
    creat()
