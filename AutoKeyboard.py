import keyboard,sys,glob


### CONFIG ###

exceptions=[","]
default_file_name="shortcuts.txt"

### END OF CONFIG ###

def read_shortcuts_file():
    '''
    Read text file content.
    :return: The shortcuts and the full words
    '''
    with open(default_file_name,'r+') as f:
        file_content=str(f.read())
        if file_content=="":
            print(f"The file '{default_file_name}' is empty.")
            sys.exit()
        lines=file_content.split('\n')
        shortcuts=[line.split(',')[0] for line in lines]
        words=[line.split(',')[1] for line in lines]
        f.close()
    return shortcuts,words

def check_valid_text():
    '''
    Check is the content in the text folder is valid fixes it otherwise
    :return: None
    '''
    with open(default_file_name, "r+") as f:
        old_text=f.read()
        lines = old_text.split('\n')

        new_text="" #first line
        words =[] #add first word
        for line in lines:
            current_word=str(line.split(',')[0])
            if current_word not in words and current_word not in exceptions:
                words.append(str(line.split(',')[0]))
                new_text+=line+"\n"
        f.close()
    if old_text!=new_text[:-1]:
        f=open(default_file_name,"w")
        f.write(new_text[:-1])
        f.close()

def is_valid_text(text):
    '''
    Checks if the text doesn't contain problematic characters
    :param text: The text to check
    :return: If the text doesn't contain problematic characters
    '''
    if len(text)==0:
        return False
    for exc in exceptions:
        if exc in text:
            return False
    return True

def check_if_file_exist():
    '''
    Checks if the text file exist in current folder
    :return: None
    '''
    if not glob.glob(default_file_name):
        print(f"Couldn't find '{default_file_name}'. Created empty file, make sure to fill it up.")
        f=open(default_file_name,'x')
        f.close()
        sys.exit()


if __name__ == '__main__':

    check_if_file_exist()

    if "-add" in sys.argv:

        if len(sys.argv) <4 or not is_valid_text(str(sys.argv[2])+str(" ".join(sys.argv[3:]))):
            print("Something went wrong make sure you use -add [shortcut] [full_word]")
            sys.exit()
        with open(default_file_name, 'r+') as f:
            text_to_write=str(sys.argv[2])+","+" ".join(sys.argv[3:])
            if f.read()!="":
                text_to_write="\n"+text_to_write
            f.write(text_to_write)
            f.close()
        print("'"+str(sys.argv[2])+","+" ".join(sys.argv[3:])+"' was added successfully!")
        exit()


    check_valid_text()
    shortcuts, words = read_shortcuts_file()

    for i in range(len(words)):
        keyboard.register_abbreviation(shortcuts[i],words[i]+" ")
    while 1:
        keyboard.wait()
