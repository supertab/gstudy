# 读取示波器保存的数据，得到幅值
# 将csv格式文件保存到data列表中
import matplotlib.pyplot as plt
import pickle

def convert_csv(csv):
    data=[]
    data_str=''
    with open(csv) as f_csv:
        for i, row in enumerate(f_csv):
            s=row.split(',')
            try:
                data_str+=s[-2]
                data.append(float(s[-2]))
            except:
                print(i)
                break
    return data

if __name__ == "__main__":
    data = convert_csv('F0002CH1.CSV')

    # wav1 = data[200:550]


    fig, (ax1,ax2,ax3) = plt.subplots(3,1,sharex=True)
    ax1.plot(data)
    ax2.set_ylim(-15,15)
    ax2.plot(data[200:550])
    ax3.set_ylim(-15,15)
    ax3.plot(data[700:1200])
    plt.show()

    # data = convert_csv('F0000CH1.CSV')
    # 保存文件
    # with open('data01.txt', 'w') as f:
        # f.write(data_str)

    # with open ('data01.plk','wb') as f:
        # pickle.dump(data, f)

    # 绘图
    # plt.plot(data)
# plt.show()
