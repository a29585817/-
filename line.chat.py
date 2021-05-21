def read_file(filename):
    lines=[]
    with open(filename , "r" , encoding="utf-8-sig") as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    chien_word_count = 0
    china_word_count = 0
    for line in lines:  
        s = line.split(" ")
        time = s[0]
        name = s[1]
        if name == "孟淳":
            for msg in s[2:]:
                china_word_count += len(msg)
        elif name == "孟謙":
            for msg in s[2:]:
                chien_word_count += len(msg)
        print(s)
    print("孟淳說了",china_word_count,"個字")
    print("孟謙說了",chien_word_count,"個字")
    # return new


def write_file(filename , lines):
    with open(filename , "w" ) as f:
        for line in lines:
            f.write(line + "\n")

def main():
    lines = read_file("[LINE]孟淳.txt")
    lines = convert(lines)
    # write_file("output.txt", lines)

main()
