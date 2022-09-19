# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

def encode(message):
    encoding = ""
    i = 0
    while i < len(message):
        count = 1
        while i + 1 < len(message) and message[i] == message[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + message[i]
        i = i + 1
    return encoding

mes = open('message.txt', 'r')
text = mes.read()
mes.close()
encText = encode(text)
text2 = open('encoding_message.txt', 'w')
text2.write(encText)
text2.close()



