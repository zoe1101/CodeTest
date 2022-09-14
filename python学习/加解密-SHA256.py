import hashlib


def get_sha256_data(inStr: str):
    """
     :param inStr: 待加密字符串
      :return: 加密结果
       """
    sha256 = hashlib.sha256()  # 实例化对象
    sha256.update(inStr.encode('utf-8'))  # 使用update方法加密
    return sha256.hexdigest()  # 调用hexdigest方法获取加密结果


if __name__ == '__main__':
    print(get_sha256_data('asfa'))
    # 输出结果
    # aaf01ca9bbd8ca8cc1703f99e62c71b56e4d01489803bf5e97bbcec646504e52