import hashlib


def get_md5_data(inStr: str):
    """
      :param inStr: 待加密字符串
      :return: 加密结果
    """
    md5 = hashlib.md5()  # 实例化对象
    md5.update(inStr.encode('utf-8'))  # 使用update方法加密
    return md5.hexdigest()  # 调用hexdigest方法获取加密结果


if __name__ == '__main__':
    print(get_md5_data('asfa'))
    # 输出结果
    # 9fa16ee8683740b1883e5844d8c288ac
