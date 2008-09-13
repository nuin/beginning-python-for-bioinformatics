def merge_seqs(data1, data2):

    myset1, myset2 = Set([]), Set([])

    for i in data1:
        myset1.add(i.name[i.name.find('|')+1:i.name.find('/')])

    for i in data2:
        myset2.add(i.name[i.name.find('|')+1:i.name.find('/')])

    mylist = Set.intersection(myset1, myset2)

    flist = []
    for i in mylist:
        for j in data1:
            if j.name[j.name.find('|')+1:j.name.find('/')] == i:
                for k in data2:
                    if k.name[k.name.find('|')+1:k.name.find('/')] == j.name[j.name.find('|')+1:j.name.find('/')]:
                        tempname = j.name + '-' + k.name + '->' + str(len(j.sequence))
                        tempseq = j.sequence + k.sequence
                        flist.append(tempname + '\n' + tempseq)

    return flist
