# from multiprocessing import Process
#
#
# def print_func(continent='Asia'):
#     print(f'Это - {continent}')
#
#
# if __name__ == '__main__':
#     names = ['America', 'Europe', 'Africa']
#     procs = []
#     proc = Process(target=print_func)
#     procs.append(proc)
#     proc.start()
#
#     for name in names:
#         proc = Process(target=print_func, args=(name,))
#         procs.append(proc)
#         proc.start()
#
#     for proc in procs:
#         proc.join()
#
# import threading
#
#
# def print_cube(num):
#     """
#     вычисляет куб от заданного числа num
#     """
#     print(f'Куб {num} -> {num * num * num}')
#
#
# def print_square(num):
#     # вычисляет куб от заданного числа num
#
#     print(f'Квадрат {num} -> {num * 2}')
#
#
# if __name__ == '__main__':
#     #создание двух потоков
#     thread1 = threading.Thread(target=print_square, args=(10,))
#     thread2 = threading.Thread(target=print_cube, args=(10,))
#     #запуск потоков
#     thread1.start()
#     thread2.start()
#
#     thread1.join() #ождание выполнения первого потока
#     thread2.join()
#
#     print('Процессы завершены')

def print_name(prefix):
    print(f' {prefix}')
    try:
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print('Корутина (coroutine) завершина')

corou = print_name('Уважаемый')
corou.__next__()
corou.send('товарищ')
corou.send('Уважаемый товарищ')
corou.close()