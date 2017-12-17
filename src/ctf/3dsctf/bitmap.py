import re
import codecs

if __name__ == '__main__':
    data = open('bitmap.txt', 'r').read()
    data = data.split("\r\n")
    reg = re.compile(r'#[a-z0-9]{6}')
    ans_file = ""
    for row in data:
        i = 0
        while i >= 0:
            m = reg.search(row, i)
            if m:
                print(row[m.start():m.end()])
                i = m.end() + 1
                ans_file += row[(m.start() + 1):m.end()]
            else:
                break
    print(ans_file)
    open('elf_file', 'wb').write(codecs.decode(ans_file, 'hex'))
