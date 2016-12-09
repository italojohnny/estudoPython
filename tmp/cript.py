import os

def main (args):
    quantify_files = len(args)

    if quantify_files < 1:
        raise ValueError("informe pelo menos um arquivo")

    for i in args:
        cripto_file = open("cifrado_"+i, "w")
        with open(i, "r") as normal_file:
            char = normal_file.read(1)
            while char:
                teste = ord(char) ^ 6
                cripto_file.write(chr(teste))
                char = normal_file.read(1)
        cripto_file.close()


if __name__ == "__main__":
    main(os.sys.argv[1:])
