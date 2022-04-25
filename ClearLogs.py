import os
import shutil

""" Get root dir """
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

""" List file for delete """
DIR_LOS_NAMES = [
    'allure_reports',
    'archived_logs',
    'latest_logs',
    'downloaded_files',
    'archived_files'
]


def getLogsPath():
    """ Clear logs after tests """
    for root, dirs, files in os.walk(ROOT_DIR):
        for dir in dirs:
            for dirLogName in DIR_LOS_NAMES:
                if dir == dirLogName:
                    shutil.rmtree(os.path.join(root, dir))


if __name__ == '__main__':
    getLogsPath()
