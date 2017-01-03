import matplotlib.pyplot as plt
def convert_txt(txt):
    with open(txt, 'r') as f:
        data_str = f.read()
        tmp = data_str.split()
        data = [float(x) for x in tmp]
    return data

data = convert_txt('data01.txt')

# plt.plot(data)
# plt.show()

