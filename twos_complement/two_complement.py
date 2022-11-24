
def two_complemts(binary):
    """
    Takes a binary string as input and returns the two's complement of that binary string
    """
    realnum = []
    for i in binary:
        realnum.append(int(i))
    for i in range(len(realnum)):
        if realnum[i] == 0:
            realnum[i] = 1
        else:
            realnum[i] = 0
    if realnum[-1] == 0:
        realnum[-1] = 1
    else:
        realnum[-1] = 0
        for i in range(len(realnum)-2, -1, -1):
            if realnum[i] == 0:
                realnum[i] = 1
                break
            else:
                realnum[i] = 0
    return ''.join(str(i) for i in realnum)

