# coding:utf-8
import os

import ffmpeg

'''
https://kkroening.github.io/ffmpeg-python/
https://blog.csdn.net/weixin_49371288/article/details/129035455
https://zhuanlan.zhihu.com/p/614892072
'''

video_file = '../../data/01_shell初步.mp4'

# 一般写法
stream = ffmpeg.input(video_file)
stream = ffmpeg.trim(stream, start=0, duration=10)  # 裁剪前十秒
stream = ffmpeg.output(stream, '../../data/01_shell初步_out1.mp4')
ffmpeg.run(stream, overwrite_output=True)


# 数据流写法
ffmpeg.input(video_file).trim(start=10, duration=20).output('../../data/01_shell初步_out2.mp4').run(overwrite_output=True)
# 或
out, _ = (
    ffmpeg
    .input(video_file)
    .trim(start=20, duration=30)
    .output('../../data/01_shell初步_out3.mp4')
    .run(overwrite_output=True)
)

# 命令行写法
'''
其中：
   -i 表示源视频文件
   -y 表示输出文件，如果已存在则覆盖

   -ss 表示从哪个时间点开始截取
   -to 表示从哪个时间点结束截取

   -vcodec copy 使用跟原视频相同的视频编解码器
   -acodec copy 使用跟原视频相同的音频编解码器

'''
out_file = '../../data/01_shell初步_out4.mp4'
os.system(f'ffmpeg -i {video_file} -ss 00:00:30 -to 00:00:40 -vcodec copy -acodec copy {out_file} -y')