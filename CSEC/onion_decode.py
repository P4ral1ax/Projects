import base64
def make_string(file):
    strings = ''
    for line in file:
        temp = line.strip('\n')
        strings += temp


    return strings


def find_base(bruh):
    temp = bruh[0:]
    base32NoNo = ['0', '1', '8', '9']
    for char in bruh:
        if char.islower():
            return '64'
    for char in bruh:
        if char in base32NoNo:
            return '16'
    return '32'

def parse(file):
    out = open("output.txt", 'w')
    bruh = make_string(file)
    temp = ''
    for i in range(0, 50):
        base = find_base(bruh)
        if base == '64':
            print("64")
            while len(bruh) % 4 != 0:
                bruh += '='
            print(len(bruh))
            bruh = base64.standard_b64decode(bruh)
            bruh = str(bruh)
            bruh = bruh[1:]
            bruh = bruh.strip("\'")
            out.write(bruh)
            out.write('\n')

        elif base == '32':
            print("32")
            while len(bruh) % 8 != 0:
                bruh += '='
            print(len(bruh))
            bruh = base64.b32decode(bruh)
            bruh = str(bruh)
            bruh = bruh[1:]
            bruh = bruh.strip("\'")
            out.write(bruh)
            out.write('\n')
        else:
            print("16")
            bruh = base64.b16decode(bruh)
            bruh = str(bruh)
            bruh = bruh[1:]
            bruh = bruh.strip("\'")
            out.write(bruh)
            out.write('\n')

    file.close()
    out.close()

def main():
    f_name = input("Type Input Data file name/path: ")
    file = open(f_name)
    parse(file)
    print("results in output file")


main()
