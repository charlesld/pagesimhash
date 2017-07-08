

from itertools import combinations
from itertools import permutations


def dedupe(items): #计算c 5 2 后的序列的组合
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def shPartSort(ccs):
    assert ccs.__len__() == 64
    dk = [2, 16, 12, 12, 12, 12]  # 划分成2,16,12,12,12,12 5份,前面2是0b tag位
    i = 0
    pack = []
    for dik in dk:
        pack.append(ccs[i:dik + i])  # 将5份数据存到pack中
        i += dik
    tag0b = pack[0]
    a = pack[1]
    b = pack[2]
    c = pack[3]
    d = pack[4]
    e = pack[5]
    ppk = ["a", "b", "c", "d", "e"]
    combins = [ci for ci in combinations(ppk, 2)]  # 组合 C 5 2
    diks = {"a": a, "b": b, "c": c, "d": d, "e": e}
    comblist = [] #存储simhash分段排序结果
    for nels in combins:
        abc = list(dedupe(list(nels)+ppk))
        # print abc #获取字符串排序后的结果
        strcombine = tag0b+diks[abc[0]]+diks[abc[1]]+diks[abc[2]]+diks[abc[3]]+diks[abc[4]] #映射到simhash分段排序
        comblist.append(strcombine)
    return comblist

if __name__ == '__main__':
    ccs = '0b11011110110000111000011100010010111000111111111110100111010110'
    print shPartSort(ccs)
    '''
    # 结果输出
    ['0b11011110110000111000011100010010111000111111111110100111010110', 
    '0b11011110110000010010111000111000011100111111111110100111010110', 
    '0b11011110110000111111111110111000011100010010111000100111010110', 
    '0b11011110110000100111010110111000011100010010111000111111111110', 
    '0b11100001110001001011100011011110110000111111111110100111010110', 
    '0b11100001110011111111111011011110110000010010111000100111010110', 
    '0b11100001110010011101011011011110110000010010111000111111111110', 
    '0b01001011100011111111111011011110110000111000011100100111010110', 
    '0b01001011100010011101011011011110110000111000011100111111111110', 
    '0b11111111111010011101011011011110110000111000011100010010111000']
    '''
