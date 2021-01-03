import time
def simple_timer(t):
    if t == 0:
        return print("Alert!!!")
    else:
        print(t,"Second")
        time.sleep(1)
        return simple_timer(t - 1)
(simple_timer(5))