def trim(S):
    n = len(S)
    start = 0
    end = n-1
    while start < n and S[start] == ' ':
        start +=1
    while end >=start and S[end] == ' ':
        end -=1
    return S[start:end+1]

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
