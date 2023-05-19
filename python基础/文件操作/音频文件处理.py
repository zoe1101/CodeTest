# Pydub是Python音频处理库，可以对音频进行切割、合并、转换、调整音量等操作。
import pydub
import pyttsx3

'''
音频生成
音频文件读取
音频文件写入
音频合成
音频切割
音频格式转换
音频属性调整
'''

# https://blog.csdn.net/weixin_43824829/article/details/127554357
def tts(text, out_path=None):
    voice = pyttsx3.init()
    voice.say(text)
    if out_path:
        voice.save_to_file(text, out_path)
    voice.runAndWait()

