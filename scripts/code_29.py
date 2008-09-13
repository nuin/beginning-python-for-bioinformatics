def read_seqs(file):
    items = []
    seq = ''
    index = 0
    for line in file:
        if line.startswith(">"):
            if index >= 1:
                items.append(seq)
                seq = ''
            index += 1
        else:
            seq += line[:-1]

    items.append(seq)
    return items
