def im_in_the_ghetto(li):
    """
    It's a reference incase you didn't get that.
    """
    for i in range(2):
        for j in range(4):
            yield li[j]

def main():
    g = list(generator(['ra', 'ta', 'ta', 'ta']))
    for i in range(8):
        print(g[i])

if __name__ == '__main__':
    main()