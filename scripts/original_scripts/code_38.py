from collections import defaultdict

def merge_seqs(data1, data2):
    first, second = defaultdict(list), defaultdict(list)
    for i in data1:
        first[i.name[i.name.find(’|')+1:i.name.find(’/')]].append(i)

    for i in data2:
        second[i.name[i.name.find(’|')+1:i.name.find(’/')]].append(i)

    shared_ids = set(first).intersection(set(second))

    flist = []
    for i in shared_ids:
        cross = ((a,b) for a in first[i] for b in second[i])
        for j, k in cross:
            tempname = j.name + ‘-’ + k.name + ‘->’ + str(len(j.sequence))
            tempseq = j.sequence + k.sequence
            flist.append(tempname + ‘\n’ + tempseq)

    return flist
