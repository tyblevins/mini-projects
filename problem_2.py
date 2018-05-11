import sys


# import random
# import string

# generate files
# with open('file1.txt', 'w+') as f:
#     [f.write(''.join(random.choices(string.ascii_lowercase + string.digits, k=32)) + '\n') for i in range(1000000)]
#
# with open('file2.txt', 'w+') as f:
#     [f.write(''.join(random.choices(string.ascii_lowercase + string.digits, k=32)) + '\n') for i in range(1000000)]

def main():
    fname = sys.argv[1]
    fname2 = sys.argv[2]

    # read first file and create hash table.
    # key is character string, value is initialized to 0.
    with open(fname, "r") as f:
        content = f.readlines()
        f.close()

    con = {x.strip(): 0 for x in content}

    # read second file.
    # for every line, check hash table for key.
    # if key exists, add one to the value
    with open(fname2, "r") as f:
        content2 = f.readlines()
        f.close()
    for line in content2:
        li = line.strip()
        try:
            con[li] = 1
        except KeyError:
            pass
    # return matches
    print(sum(con.values()))


if __name__ == '__main__':
    main()
