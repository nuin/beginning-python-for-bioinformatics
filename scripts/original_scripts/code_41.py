def merge_seqs(data1, data2):
    from itertools import chain, groupby
    format = "%s-%s->%d\n%s%s"
    flist = []
    keyfunc = lambda it: it.name[it.name.find('|') + 1 : it.name.find('/')]
    for it, g in groupby(sorted(chain(data1, data2), key=keyfunc), keyfunc):
        values = list(g)
        if len(values) == 2:
            jname, jseq = values[0].name, values[0].sequence
            kname, kseq = values[1].name, values[1].sequence
            flist.append(format % (jname, kname, len(jseq), jseq, kseq) )

    return flist
