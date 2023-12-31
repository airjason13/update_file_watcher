import re
from global_def import *


def check_swu_file_name_format(file_name : str):
    if file_name.startswith("Eduarts") is False:
        log.debug("file_name Eduarts Error : %s", file_name)
        return False
    m = []
    try:
        m = re.match(r'(\S+)_(\d+)_(\d+)_(\d+)_(\d+)_(\d+).swu', file_name)
    except Exception as e:
        log.debug(e)
        return False

    if m is None:
        log.debug("%s name format not correct", file_name)
        return False
    log.debug("%s", m.groups())

    try:
        name = file_name.split(".swu")
        n = re.split('_', name[0])
        '''compare year'''
        if int(n[1]) < 2022 or int(n[1]) > 2123:
            return False
        '''compare month'''
        if int(n[2]) < 1 or int(n[2]) > 12:
            return False
        '''compare day'''
        if int(n[3]) < 1 or int(n[3]) > 31:
            return False

    except Exception as e:
        log.debug(e)
        return False


    log.debug("n : %s", n)
    log.debug("%s name format correct", file_name)
    return True


'''
parameter : swu file uri list
Steps :
1. get file name from list and append the file name to file name list
2. compare the least file name
3. return the least swu file uri
'''


def get_least_swu_file_uri(swu_file_list: list[str]) -> str:
    swu_file_name_list = []
    for swu_file in swu_file_list:
        tmp = swu_file.split("/")
        swu_file_name = tmp[len(tmp) - 1]
        swu_file_name_list.append(swu_file_name)
    
    log.debug("and got ")
    for file_name in swu_file_name_list:
        log.debug("%s", file_name)
    log.debug("in file name list")
    least_file_name = ''

    for file_name in swu_file_name_list:
        if file_name > least_file_name:
            least_file_name = file_name

    for swu_file in swu_file_list:
        if least_file_name in swu_file:
            return swu_file

    return None
