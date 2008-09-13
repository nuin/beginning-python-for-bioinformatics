def merge_seqs(data1, data2):
    first, second = dict(), dict()
    for i in data1:
        first[i.name[i.name.find('|') + 1:i.name.find('/')]] = i

    for i in data2:
        second[i.name[i.name.find('|') + 1:i.name.find('/')]] = i

    shared_ids = set(first).intersection(set(second))

    flist = []
    for i in shared_ids:
        j = first[i]
        k = second[i]
        tempname = j.name + '-' + k.name + '-&gt;' + str(len(j.sequence))
        tempseq = j.sequence + k.sequence
        flist.append(tempname + '\n' + tempseq)

    return flist
