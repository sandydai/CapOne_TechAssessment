import os

class Language: #Language stores information about language

    def __init__(self):
        self.lang = ""
        self.ext = ""
        self.block_begin = ""
        self.block_end = ""
        self.inline = ""
        self.no_block = False

    def set_info(self, lang, ext, begin, end, inline, no_block):
        self.lang = lang
        self.ext = ext
        self.block_begin = begin
        self.block_end = end
        self.inline = inline
        self.no_block = no_block

    def get_lang(self):
        return self.lang

    def get_ext(self):
        return self.ext

    def get_block_begin(self):
        return self.block_begin

    def get_block_end(self):
        return self.block_end

    def get_inline(self):
        return self.inline

    def get_noblock(self):
        return self.no_block


class LanguageList: # Map of languages
    lang_dict = {}  # dictionary maps language name to language

    def __init__(self):
        self.lang_dict = {}

    def add_lang(self, lang, ext, begin, end, inline, no_block):
        new_lang = Language()
        new_lang.set_info(lang, ext, begin, end, inline, no_block)
        temp = new_lang.get_lang()
        self.lang_dict[temp] = new_lang

    def get_lang(self):
        return self.lang_dict.keys()

    def get_data(self):
        return self.lang_dict


def main(path):

    curr_list = LanguageList() #initialized with common languages
    curr_list.add_lang("java", ".java", "/*", "*/", "//", False)
    curr_list.add_lang("python", ".py", "'''", "'''", "#", True)
    curr_list.add_lang("ruby", ".rb", "=begin", "=end", "#", False)
    curr_list.add_lang("c++", ".cpp", "/*", "*/", "//", True)

    name = os.path.splitext(path)[0]
    if name[0] == ".":
        raise ValueError("File-type not accepted, please check the file name")
    extension = os.path.splitext(path)[1]
    temp = curr_list.get_data()

    lang = ""

    for key in curr_list.get_data():
        if extension in temp[key].get_ext():
            lang = key
            break
    if lang == "":
        raise ValueError("File-type not accepted, language not recognized. Please update LanguageList.")
    curr_lang = temp[key]
    # set variables and counts
    start = curr_lang.get_block_begin()
    end = curr_lang.get_block_end()
    inline = curr_lang.get_inline()
    num_todo, num_lines, num_inline, num_block, num_block_comm = 0, 0, 0, 0, 0
    in_block = False

    for line in open(path, 'r').readlines():
        # check for block comments
        x = str(line)
        a = x.find(start)
        if a != -1:
            in_block = True
        if in_block is True:
            num_block_comm += 1
        # check for end
        b = x.find(end)
        if b != -1:
            in_block = False
            num_block += 1


        # check for inline comments
        c = x.find(inline)
        if c != -1:
            num_inline += 1


        # check for todo
        d = x.find("TODO")
        if d != -1:
            num_todo += 1

        num_lines += 1

    total_comm = num_block_comm + num_inline

    return num_lines, total_comm, num_block, num_block_comm, num_inline, num_todo



if __name__ == '__main__':
    num_lines, total_comm, num_block, num_block_comm, num_inline, num_todo = main("Index.java")
    print("Total  # of lines: " + str(num_lines))
    print("Total  # of comment lines: " + str(total_comm))
    print("Total  # of single line comments: " + str(num_inline))
    print("Total  # of comment lines within block comments: " + str(num_block_comm))
    print("Total  # of block line comments: " + str(num_block))
    print("Total  # of TODO’s: " + str(num_todo))




















