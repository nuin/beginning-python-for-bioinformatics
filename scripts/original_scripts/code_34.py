def parse_entry(gene_data):
    #changes a string to list, splitting at line ends
    gene_data = gene_data.split('\n')
    start, end = 0, 0
    gi_id = ''
    id = ''
    complement = False
    for line in gene_data:
        if line.find('  CDS  ') >=0:
            temp = line.split()
            if temp[1].find('complement') >= 0:
                complement = True
                temp[1] = temp[1].replace('complement(', '')
                temp[1] = temp[1].replace(')', '')
            temp2 = temp[1].split('..')
            start = temp2[0]
            end = temp2[1]
        elif line.find('GI:') >= 0:
            gi_id = 'gi' + line[line.find('GI:')+3:-1]
        elif line.find('/product') >=0:
            id = line[line.find('=') + 2:-1]
        elif line.find('protein_id') >= 0:
            id += '\t' + line[line.find('=') + 2: -1]

    return CDSinfo(gi_id, id, start, end, complement)
