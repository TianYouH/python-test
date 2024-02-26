file = open("静夜思.txt", "r", encoding="utf-8")

# print(file.readable()) # 判断文件是否可读
# print(file.writable()) # 判断文件是否可写
# print(file.seekable()) # 判断文件是否可定位


# read() 一次性读取文件所有内容
# content = file.read()
# print("1", content)

# readline() 读取一行内容
# while True:
#     content_2 = file.readline()
#     if not content_2:
#         break
#     print("2", content_2)

# readlines() 读取所有行内容，返回一个列表
# content_3 = file.readlines()
# for i in content_3:
#     print("3", i)

# 读取文件内容并写入到另一个文件
# out_file = open("静夜思_副本.txt", "w", encoding="utf-8")
# line_num = 1
# for line in file:
#     out_file.write(str(line_num) + " " + line)
#     line_num += 1
# out_file.close()

file.close()