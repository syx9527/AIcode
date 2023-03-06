import logging
import os
import sys

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir = os.path.join(root_dir, "logs")

if not os.path.exists(log_dir):
    os.mkdir(log_dir)

def _get_logger():
    log = logging.getLogger('log')
    log.setLevel(logging.INFO)
    console_handle = logging.StreamHandler(sys.stdout)
    console_handle.setFormatter(logging.Formatter('[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] - %(message)s',
                                                  datefmt='%Y-%m-%d %H:%M:%S'))
    # 创建处理器：sh为控制台处理器，fh为文件处理器,log_file为日志存放的文件夹
    # log_file = os.path.join(log_dir,"{}_log".format(time.strftime("%Y/%m/%d",time.localtime())))
    log_file = os.path.join(log_dir, "autotest.log")
    fh = logging.FileHandler(log_file, encoding="UTF-8")

    # 创建格式器,并将sh，fh设置对应的格式
    formator = logging.Formatter('[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] - %(message)s',
                                                  datefmt='%Y-%m-%d %H:%M:%S')
    fh.setFormatter(formator)

    log.addHandler(console_handle)
    log.addHandler(fh)
    return log


# 日志句柄
logger = _get_logger()