# Pydub��Python��Ƶ����⣬���Զ���Ƶ�����и�ϲ���ת�������������Ȳ�����
import pydub
import pyttsx3

'''
��Ƶ����
��Ƶ�ļ���ȡ
��Ƶ�ļ�д��
��Ƶ�ϳ�
��Ƶ�и�
��Ƶ��ʽת��
��Ƶ���Ե���
'''

# https://blog.csdn.net/weixin_43824829/article/details/127554357
def tts(text, out_path=None):
    voice = pyttsx3.init()
    voice.say(text)
    if out_path:
        voice.save_to_file(text, out_path)
    voice.runAndWait()

