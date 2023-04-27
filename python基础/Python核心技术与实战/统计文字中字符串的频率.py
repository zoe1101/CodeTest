
import re
# 参考：https://www.cnblogs.com/geogre123/p/10931557.html
def solution1(text):
    '''
    假如有有in.txt文件，读文件进行词频统计
    需求：
    1.读取文件
    2.去除所有标点符号和换行符，并把所有大写变成小写；
    3.合并相同的词，统计每个词出现的频率，并按照词频从大到小排序；
    4.将结果按行输出到文件out.txt。
    '''
    text=re.sub(r'[^\w ]', ' ', text) # 使用正则表达式去除标点符号和换行符
    text=text.lower() # 转为小写
    word_list=text.split()
    word_list=filter(None,word_list) # 去除空白单词

    # 生成单词和词频的字典
    word_cnt={}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word]=0
        word_cnt[word]+=1
    word_cnt=sorted(word_cnt.items(),key=lambda kv: kv[1],reverse=True)
    return word_cnt

def solution2():
    '''
    思考题1
第一问：你能否把 NLP 例子中的 word count 实现一遍？不过这次，in.txt 可能非常非常大（意味着你不能一次读取到内存中），而 output.txt 不会很大（意味着重复的单词数量很多）。
提示：你可能需要每次读取一定长度的字符串，进行处理，然后再读取下一次的。但是如果单纯按照长度划分，你可能会把一个单词隔断开，所以需要细心处理这种边界情况。
    :return:
    '''
    CHUNK_SIZE = 100  # 这个数表示一次最多读取的字符长度
    def parse_to_word_list(text, last_word, word_list):
        text = re.sub(r'[^\w ]', ' ', last_word + text)
        text = text.lower()
        cur_word_list = text.split(' ')
        cur_word_list, last_word = cur_word_list[:-1], cur_word_list[-1]
        word_list += filter(None, cur_word_list)
        return last_word

    def solve():
        with open('in.txt', 'r') as fin:
            word_list, last_word = [], ''
            while True:
                text = fin.read(CHUNK_SIZE)
                if not text:
                    break  # 读取完毕，中断循环
                last_word = parse_to_word_list(text, last_word, word_list)

            word_cnt = {}
            for word in word_list:
                if word not in word_cnt:
                    word_cnt[word] = 0
                word_cnt[word] += 1

            sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)
            return sorted_word_cnt

    print(solve())

if __name__ == '__main__':
    with open('in.txt','r') as f:
        text=f.read()
    word_cnt=solution1(text)

    with open('out.txt', 'w') as f:
        for word, freq in word_cnt:
            f.write('{} {}\n'.format(word, freq))


