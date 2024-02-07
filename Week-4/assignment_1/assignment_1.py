from threading import *
from time import sleep


def do_job(number):
    sleep(3)
    print(f"Job {number} finished")


# rewrite everything inside this main function and keep others untouched
def main():
    thread_ls = []

    for i in range(5):
        thread = Thread(target=do_job, args=(i,))  # create a thread and specify the function
        thread_ls.append(thread)
        thread.start()
        sleep(0.1)
    for t in thread_ls:
        t.join()    

    # Option 2 takes longer as the join() holds thread till the next round
    # for t in thread_ls:
    #     t.start()
    #     sleep(0.1)
    # for t in thread_ls:
    #     t.join()


main()
