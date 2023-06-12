# encoding = utf-8

import sys, pathlib, fitz

if __name__ == "__main__":

    # pdf to txt
    fname = sys.argv[1]  # get document filename
    with fitz.open(fname) as doc:  # open document
        text = chr(12).join([page.get_text() for page in doc])
    # write as a binary file to support non-ASCII characters
    pathlib.Path(fname + ".txt").write_bytes(text.encode())

    # Count
    word_dict_fname = sys.argv[2]
    f = open(word_dict_fname, "r", encoding = "utf-8")
    word_dict = f.read().strip().split('\n')
    fname = fname + '.txt'
    count = dict()
    for word in word_dict:
        count[word] = 0
    with open(fname, "r", encoding = "utf-8") as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                if word in word_dict:
                    count[word] += 1

    with open("{}_output.txt".format(fname.split('.')[0]), "w", encoding = "utf-8") as fo:
        fo.write("File name: {}\n".format(fname[:-4]))
        fo.write("Key word Statistics:\n")
        for key, value in count.items():
            fo.write("{}: {}\n".format(key, value))

    print("Done.")