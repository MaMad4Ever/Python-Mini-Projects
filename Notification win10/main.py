import win10toast
import time


pop = win10toast.ToastNotifier()
pop.show_toast("Notification","Alert!!! Virus Found")

while pop.notification_active():
    time.sleep(1)
