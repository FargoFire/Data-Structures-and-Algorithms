# -*- coding: utf-8 -*-

"""
    Date: 2018/11/25
    By: Fargo
    哈希算法：将任意长度的二进制值串映射为固定长度的二进制值串，这个映射的规则就是哈希算法，
              而通过原始数据映射之后得到的二进制值串就是哈希值。

"""
from hashlib import md5

A = 'd131dd02c5e6eec4693d9a0698aff95c' \
    '2fcab58712467eab4004583eb8fb7f89' \
    '55ad340609f4b30283e488832571415a' \
    '085125e8f7cdc99fd91dbdf280373c5b' \
    'd8823e3156348f5bae6dacd436c919c6' \
    'dd53e2b487da03fd02396306d248cda0' \
    'e99f33420f577ee8ce54b67080a80d1e' \
    'c69821bcb6a8839396f9652b6ff72a70'
B = 'd131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70'

A_md5 = md5()
B_md5 = md5()

# # 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
A_md5.update(A.encode(encoding= 'utf-8'))
B_md5.update(B.encode(encoding= 'utf-8'))

A_hash = A_md5.hexdigest()   # 32位的16进制 ，128bit
B_hash = B_md5.hexdigest()

print(A_hash, len(A_hash))
print(B_hash )

B_int = int(B_hash[:2])
c = B_int /3
print(c)