import numpy as np
# str2int
# give a set for int and a bit string each member of the set
# is show the count split for the string, convert
# string to another set of int, 

def bitstr2int(bs, kset):
    # bs: bit stream generate by the VQ index
    # kset: k bits to represent the VQ dictionary
    idx = []
    i = 0
    for c in kset:
        tmp = bs[i: i+c]
        idx.append(int(tmp,2))
        i += c
    return np.array(idx)

# int2str
# convert int to bit string then connect them
def int2bitstr(idxset, kset):
    # idxset: the index of each vector in VQ dictionary
    # kset: k bits to represent the VQ dictionary
    bs = ''
    for i,c in zip(idxset, kset):
        tmp = bin(i)[2:] # remove 0b
        bitlen = len(tmp)
        if bitlen < c:
            nzero = c - bitlen
            tmp = '0'*nzero + tmp
        bs += tmp
    return bs

if __name__ == '__main__':
    k = (2, 3, 9, 2) # set of int
    idxset = (1, 5, 301, 0)
    s = "0110110010110100"
    print('bit allocate:', k)
    print('In: bitstream: %s\nOut: bitstr2int: %s'%(s, bitstr2int(s, k)))
    print('In: idxset: %s,\nOut: int2bitstr: %s'%(idxset, int2bitstr(idxset, k)))

