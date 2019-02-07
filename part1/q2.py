import sys

if __name__ == "__main__":
    pato = sys.argv[1]
    taku = sys.argv[2]

    patotaku = ''
    for p, t in zip(pato, taku):
        patotaku += p + t

    print(patotaku)