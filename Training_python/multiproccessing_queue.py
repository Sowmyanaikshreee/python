import multiprocessing


def cal_square(numbers,q):
    for i in numbers:
        q.put(i*i)

if __name__ == "__main__":
    numbers = [2,3,4]
    q=multiprocessing.Queue()
    p = multiprocessing.Process(target=cal_square, args=(numbers,q))

    p.start()
    p.join()

    while q.empty()  is False:
        print(q.get())
