# coding: utf-8
import os.path
import pyttsx3
import soundfile as sf
import numpy as np
from pydub import AudioSegment  # Pydub是Python音频处理库，可以对音频进行切割、合并、转换、调整音量等操作。

'''
音频生成
音频文件读取：音频格式：wav、pcm、mp3、wma等
音频文件写入
音频合并
音频切割
音频格式转换
音频属性调整
'''


# https://blog.csdn.net/weixin_43824829/article/details/127554357
def tts(text, out_path=None):
    '''
    语音生成
    :param text:
    :param out_path:
    :return:
    '''
    voice = pyttsx3.init()
    voice.say(text)
    if out_path:
        voice.save_to_file(text, out_path)
    voice.runAndWait()


def read_audio(file):
    '''
    语音读取
    :param file:
    :return:
    '''
    ext = os.path.splitext(file)[-1].lower()
    audio = AudioSegment.from_file(file, format=ext)
    return audio


def play_audio(audio):
    '''
    语音播放
    :param audio:
    :return:
    '''
    from pydub.playback import play
    play(audio)


def save_audio(audio, out_path, format):
    audio.export(out_path, format=format.strip('.').lower())


def segment_audio(audio, start=None, end=None):
    '''
    语音切割
    :param audio:
    :param start:
    :param end:
    :return:
    '''
    if start and end:
        return audio[start:end]
    elif start:
        return audio[start:]
    elif end:
        return audio[:end]
    else:
        return audio


def concat_audio(files, out_path):
    '''
    语音拼接
    :param files:
    :param out_path:
    :return:
    '''
    audio_list = []
    for f in files:
        audio_list.append(read_audio(f))

    concat_audio = audio_list[0]
    for ad in audio_list[1:]:
        concat_audio += ad
    save_audio(concat_audio, out_path, os.path.splitext(out_path)[-1])


def mix_audio(files, out_path):
    '''
    语音混合叠加
    :param files:
    :param out_path:
    :return:
    '''
    audio_list = []
    for f in files:
        audio_list.append(read_audio(f))

    mix_audio = audio_list[0]
    for ad in audio_list[1:]:
        mix_audio.overlay(ad)
    save_audio(mix_audio, out_path, os.path.splitext(out_path)[-1])


def format_conversion(file, out_path, format):
    '''
    格式转换
    :param file:
    :param format:
    :return:
    '''
    audio = AudioSegment.from_file(file)
    filename = os.path.splitext(os.path.basename(file))[0]
    save_audio(audio, os.path.join(out_path, filename + format), format)


if __name__ == '__main__':
    # tts('吃了吗', '../../data/吃了吗.wav')
    # read_audio('../../data/吃了吗.wav')
    format_conversion('../../data/吃了吗.wav', '../../data/', '.raw')
