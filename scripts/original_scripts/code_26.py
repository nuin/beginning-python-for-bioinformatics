class Fasta:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

def read_fasta(file):
    items = []
    index = 0
    for line in file:
        if line.startswith(">"):
           if index >= 1:
               items.append(aninstance)
           index += 1
           name = line[:-1]
           seq = ''
           aninstance = Fasta(name, seq)
        else:
           seq += line[:-1]
           aninstance = Fasta(name, seq)

    items.append(aninstance)
    return items
