import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name,'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())




filenames = [f'./file {number}.txt' for number in range(1, 5)]


# start = datetime.datetime.now()
# for name in filenames:
#     read_info(name)
# stop = datetime.datetime.now()
# print(f'Линейное выполнение: {stop - start} секунд')
#Линейное выполнение: 0:00:13.235685 секунд

if __name__ == '__main__':
    start = datetime.datetime.now()
    with Pool() as pool:
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        pool.map(read_info, filenames)
    stop = datetime.datetime.now()
    print(f'Многопроцессорное выполнение: {stop - start} секунд')

#Многопроцессорное выполнение: 0:00:08.255196 секунд
