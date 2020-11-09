import keyboard


def read_shortcuts_file():
    with open("shortcuts.txt",'r') as f:
        lines=f.read().split('\n')
        shortcuts=[i.split(',')[0] for i in lines]
        words=[i.split(',')[1] for i in lines]
        f.close()
    return shortcuts,words

def check_valid_text():
    with open("shortcuts.txt", "r+") as f:
        old_text=f.read()
        lines = old_text.split('\n')

        new_text=lines[0] #first line
        words =[lines[0].split(',')[0]] #add first word
        for line in lines:
            current_word=line.split(',')[0]
            if current_word not in words and current_word!="":
                words.append(line.split(',')[0])
                new_text+="\n"+line
        if old_text!=new_text:
            f.truncate(0)
            f.write(new_text)
        f.close()

check_valid_text()
shortcuts,words=read_shortcuts_file()

for i in range(len(words)):
    keyboard.register_abbreviation(shortcuts[i],words[i])

while 1:
    keyboard.wait()

