poem = '''
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# 打开&创建文件
f = open('test.text', 'w')

# 写入
f.write(poem)

# 关闭
f.close()

# 如果没有指定文件打开方式
# 默认使用 'r'ead 读模式  r-只读  w-读写 a-追加
f = open('test.text')

while True:
    line = f.readline()
    # 零行意味着 EOF 文件结尾
    if len(line) == 0:
        break
    print(line, end='')

f.close()
