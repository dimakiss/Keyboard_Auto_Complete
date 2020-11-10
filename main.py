import keyboard,sys


def read_shortcuts_file():
    with open("shortcuts.txt",'r') as f:
        lines=f.read().split('\n')
        shortcuts=[i.split(',')[0] for i in lines]
        words=[i.split(',')[1] for i in lines]
        f.close()
    return shortcuts,words

def check_valid_text():
    with open("shortcuts.txt", "r+") as f:
        old_text=str(f.read())
        lines = old_text.split('\n')

        new_text="" #first line
        words =[] #add first word
        for line in lines:
            current_word=line.split(',')[0]
            if current_word not in words and current_word!="":
                words.append(str(line.split(',')[0]))
                new_text+=line+"\n"
        if old_text!=new_text[:-1]:
            f.truncate(0)
            f.write(new_text[:-1])
        f.close()




if __name__ == '__main__':

    #sys.argv=['main.py', '-add', 'k', 'kkkk']
    if "-add" in sys.argv:
        if len(sys.argv) !=4 or not str(sys.argv[2]).isalpha() or not str(sys.argv[3]).isalpha():
            print("Something went wrong make sure you use -add shortcut full_word")
            sys.exit()
        with open("shortcuts.txt", 'r+') as f:
            text_to_write=str(sys.argv[2])+","+str(sys.argv[3])
            if f.read()!="":
                text_to_write=str(f.read())+"\n"+text_to_write
            f.write(text_to_write)
            f.close()
        exit()

    check_valid_text()
    shortcuts, words = read_shortcuts_file()

    for i in range(len(words)):
        keyboard.register_abbreviation(shortcuts[i], words[i])

    while 1:
        keyboard.wait()

