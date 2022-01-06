'''
可以方便地序列化/逆序列化结构数据。YAMLObject 的一个超越变形能力，
就是它的任意子类支持序列化和反序列化（serialization & deserialization）
'''
import yaml
class Monster(yaml.YAMLObject):
  yaml_tag = u'!Monster'
  def __init__(self, name, hp, ac, attacks):
    self.name = name
    self.hp = hp
    self.ac = ac
    self.attacks = attacks
  def __repr__(self):
    return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
       self.__class__.__name__, self.name, self.hp, self.ac,
       self.attacks)

monster1 = yaml.load("""
--- !Monster
name: Cave spider
hp: [2,6]    # 2d6
ac: 16
attacks: [BITE, HURT]
""",Loader=yaml.Loader)

print(monster1)
#Monster(name='Cave spider', hp=[2, 6], ac=16, attacks=['BITE', 'HURT'])
print(type(monster1)) #<class '__main__.Monster'>


print (yaml.dump(Monster(
    name='Cave lizard', hp=[3,6], ac=16, attacks=['BITE','HURT']))
)

# dump() 返回 str
# 输出
# !Monster
# ac: 16
# attacks: [BITE, HURT]
# hp: [3, 6]
# name: Cave lizard