from global_def import *
import os
import usbfilewatcher


class UsbUpdateWorker:

    def __init__(self, **kwargs):
        user_name = os.getlogin()
        log.debug("user_name : %s", user_name)
        path = "/media/" + user_name
        self.watch_paths = [path]  # ["/media/venom"]
        self.updatefilewatcher = None

        try:
            self.updatefilewatcher = usbfilewatcher.UpdateFileWatcher(self.watch_paths, self.show_notification_path)
        except Exception as e:
            log.fatal(e)

    def show_notification_path(self, path : str):
        log.debug("got notification from %s", path)
        # self.swu_file_list.clear()
        # self.get_swu_file_list(path)
