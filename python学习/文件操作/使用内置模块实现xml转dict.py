#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET
import json


def xml2dict(node):
    if not isinstance(node, ET.Element):
        raise Exception("node format error.")

    if len(node) == 0:
        return node.tag, node.text

    data = {}
    temp = None
    for child in node:
        key, val = xml2dict(child)
        if key in data:
            if type(data[key]) == list:
                data[key].append(val)
            else:
                temp = data[key]
                data[key] = [temp, val]
        else:
            data[key] = val

    return node.tag, data


if __name__ == '__main__':
    xmldata = ET.parse('../../data/testxml2dict.xml')
    node = xmldata.getroot()
    print('原始xml数据：\n', node)
    tag, data = xml2dict(node)
    print('转换后的dict数据：\n', tag, data)
