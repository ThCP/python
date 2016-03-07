def fixed_length_encoder(codebook, Nsymb, x):
    msg=''

    encoded = []
    for i in range (0, Nsymb):
        encoded.append(codebook[x[i]])
    #print encoded

    return encoded

def huffman_encoder(codebook, Nsymb, x):
    msg=''

    encoded = []
    for i in range (0, Nsymb):
        encoded.append(codebook[x[i]])
    #print encoded

    return encoded

def generic_encoder(codebook, Nsymb, x):
    msg=''

    encoded = []
    for i in range (0, Nsymb):
        encoded.append(codebook[x[i]])
    #print encoded

    return encoded
