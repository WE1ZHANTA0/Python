import os
import time

# 1. 将要备份的文件和目录分配到一个列表中
# Windows 例子
# source = ['"C:\\My Documents"']
# Mac OS X 和 Linux 例子:
source = ['/Users/weizhantao/WZT/20200629share']
# 注意如果名字中包含空格我们需要用复数引号
# 或者用 raw 字符串  [r'C:\My Documents'].

# 2. 必须备份到主目录中
# Windows 例子:
# target_dir = 'E:\\Backup'
# Mac OS X 和 Linux 例子:
target_dir = '/Users/weizhantao/WZT/copyShare'


# 如果目录不存在则创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # 创建目录

# 3. 文件需要备份到 zip 里。
# 4. zip 的名字需要是当前的日期+时间。
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 当前时间作为备份文件的文件名
now = time.strftime('%H%M%S')

# 让用户输出一个用于创建 zip 文件的名字。
comment = input('Enter a comment -->')
# 检测是否有comment
if len(comment):
    target = today + os.sep + comment + '.zip'
else:
    target = today + os.sep + now + '_' +\
             comment.replace(' ', '_') + '.zip'

# 如果不存在创建子文件夹
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5. 使用 zip 命令把文件放到 zip 里。
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

# 运行
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
