from easyfilewatcher.EasyFileWatcher import EasyFileWatcher
from global_def import *
import os
import utils.file_utils

class UpdateFileWatcher:
    def __init__(self, paths, cb, **kwargs):
        self.filewatcher = EasyFileWatcher()
        self.watch_paths = paths
        self.watch_count = 0
        self.callback = cb
        self.swu_file_list = []
        for path in self.watch_paths:
            self.filewatcher.add_directory_to_watch(directory_path=path,
                                                    directory_watcher_id=path, callback=self.file_notification,
                                                    callback_param={'msg': path}, event_on_deletion=True)

    def file_notification(self, msg: str):
        log.debug(msg)
        self.swu_file_list.clear()
        self.get_swu_file_list(msg)
        if len(self.swu_file_list) > 0:
            least_swu_file_uri = utils.file_utils.get_least_swu_file_uri(self.swu_file_list)
            self.callback(least_swu_file_uri)

    def get_swu_file_list(self, path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                if '.swu' in name:
                    if utils.file_utils.check_swu_file_name_format(name):
                        log.debug("os.path.join(root, name) : %s", os.path.join(root, name))
                        if 'Trash' not in os.path.join(root, name):
                            self.swu_file_list.append(os.path.join(root, name))
                            log.debug("file name : %s", name)
                            log.debug("os.path.join(root, name) : %s", os.path.join(root, name))

        log.debug("*******************************************************")
        log.debug("we got")
        for swu_file in self.swu_file_list:
            log.debug("%s", swu_file)

        log.debug("in swu file list")
        return len(self.swu_file_list)

    def quit(self):
        for path in self.watch_paths:
            self.filewatcher.delete_easy_file_watcher(path)
