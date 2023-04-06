#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xmltodict


def xml2dict(xmldata, moudle):
    """
    xml转dict
    xmldata: xml字符串
    moudle:根节点
    return: dict字符串
    """
    data = xmltodict.parse(xmldata, process_namespaces=True)
    dictdata = dict(data)
    _dictdata = dict(dictdata[moudle])
    dictdata[moudle] = _dictdata
    return dictdata


def dict2xml(dictdata):
    """
    dict转xml
    dictdata: dict字符串
    return: xml字符串
    """
    xmldata = xmltodict.unparse(dictdata, pretty=True)
    return xmldata


if __name__ == '__main__':
    xmldata = open('../../data/testxml2dict.xml', 'r', encoding='utf-8').read()
    print('原始xml数据：\n', xmldata)
    dictdata = xml2dict(xmldata, 'mydocument')
    print('转换后的dict数据：\n', dictdata)
    xmldata = dict2xml(dictdata)
    print('转换后的xml数据：\n', xmldata)
