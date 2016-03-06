def fixed_length_encoder(codebook, Nsymb, x):
    msg=''

    encoded_y1 = []
    for i in range (0, Nsymb):
        encoded_y1.append(codebook[x[i]])
    print encoded_y1

    return encoded_y1