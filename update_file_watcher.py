# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import usbfilewatcher
import time
from global_def import *
import os
import glob
import usbupdateworker

def get_file_list(path):
    swu_file_list = []  # contains path, means uri
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            # print(os.path.join(root, name))
            if '.swu' in name:
                swu_file_list.append(os.path.join(root, name))
                log.debug("file name : %s", name)
                log.debug("os.path.join(root, name) : %s", os.path.join(root, name))

    log.debug("*******************************************************")
    log.debug("we got")
    for swu_file in swu_file_list:
        log.debug("%s", swu_file)


def show_notification_path(path : str):
    log.debug("got notification from %s", path)
    get_file_list(path)


def clear_sqlite():
    path = os.getcwd()
    if os.path.isfile(path + "/easyfilewatcher.sqlite"):
        os.remove(path + "/easyfilewatcher.sqlite")
    if os.path.isfile(path + "/jobs.sqlite"):
        os.remove(path + "/jobs.sqlite")


if __name__ == '__main__':
    usbupdateworker = usbupdateworker.UsbUpdateWorker()
    while True:
        time.sleep(1)

'''
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user_name = os.getlogin()
    log.debug("user_name : %s", user_name)
    path = "/media/" + user_name
    watch_paths = ["/media/venom"]
    # clear_sqlite()
    try:
        updatefilewatcher = usbfilewatcher.UpdateFileWatcher(watch_paths, show_notification_path)
    except Exception as e:
        log.fatal(e)
    while True:
        time.sleep(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''