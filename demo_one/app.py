import threading


""" Thread is a mean by which a program of app can excectue various function simutanously """

def thread_one_function(test_arg_one, test_arg_two):
    for i in range(0, 20):
        print(f'I am Tread one ----- {test_arg_one}, {test_arg_two}')

def thread_two_function(test_agr):
    for i in range(0, 20):
        print(f"I am thread two {test_agr}")
    

# Here i am initailizing the threading Tread class
thread_1 = threading.Thread(target=thread_one_function, args=("one", "two", ))
thread_2 = threading.Thread(target=thread_two_function, args=(2, ))

# Starting up the thread
thread_2.start()
thread_1.start()

# Creating a mechinsm that would make the interpreter wait till the thread is excecuted
thread_1.join()
thread_2.join()