import sys
sys.path.append('./lbc')
import lbc
import pickle

item = '''[0] training samples
[1] image encode
[2] image decode
enter: '''

chs = input(item)
chs = int(chs)

blksize = 8
imgsize = 512
k = 5
img_name = 'testIMG/0493.bmp'
sampleDIR = 'sample/'
bksetDIR = 'blocks/'

if chs==0:
    # training
    kset = k
    vqds  = lbc.train.vq_train(sampleDIR, bksetDIR, kset, imgsize, blksize, gen_set=False, sav=True)

elif chs==1:
    # encoding
    with open('vqdict.pkl','rb') as f:
        vqds = pickle.load(f)
    kset = [k]*len(vqds)
    hexcode = lbc.encode.encode(img_name, vqds, kset, imgsize, blksize)

elif chs==2:
    # decoding
    with open('vqdict.pkl','rb') as f:
        vqds = pickle.load(f)
    kset = [k]*len(vqds)
    hexfile = img_name[:-3] + 'hex'
    bitstream  = lbc.decode.hex2bit(hexfile)
    img = lbc.decode.decode(bitstream, vqds, kset, imgsize, blksize)
    lbc.decode.img_show_save(img, hexfile, show=True, sav=True)
