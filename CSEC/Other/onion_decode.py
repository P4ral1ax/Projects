import base64
def make_string(file):
    strings = ''
    for line in file:
        temp = line.strip('\n')
        strings += temp


    return strings


def find_base(cipher):
    temp = cipher[0:]
    base32NoNo = ['0', '1', '8', '9']
    for char in cipher:
        if char.islower():
            return '64'
    for char in cipher:
        if char in base32NoNo:
            return '16'
    return '32'

def parse(file):
    out = open("output.txt", 'w')
    cipher = make_string(file)
    temp = ''
    for i in range(0, 50):
        base = find_base(cipher)
        if base == '64':
            print("64")
            while len(cipher) % 4 != 0:
                cipher += '='
            print(len(cipher))
            cipher = base64.standard_b64decode(cipher)
            cipher = str(cipher)
            cipher = cipher[1:]
            cipher = cipher.strip("\'")
            out.write(cipher)
            out.write('\n')

        elif base == '32':
            print("32")
            while len(cipher) % 8 != 0:
                cipher += '='
            print(len(cipher))
            cipher = base64.b32decode(cipher)
            cipher = str(cipher)
            cipher = cipher[1:]
            cipher = cipher.strip("\'")
            out.write(cipher)
            out.write('\n')
        else:
            print("16")
            cipher = base64.b16decode(cipher)
            cipher = str(cipher)
            cipher = cipher[1:]
            cipher = cipher.strip("\'")
            out.write(cipher)
            out.write('\n')

    file.close()
    out.close()

def main():
    f_name = input("Type Input Data file name/path: ")
    file = open(f_name)
    parse(file)
    print("results in output file")


main()
