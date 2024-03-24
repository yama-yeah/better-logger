
from logging import StreamHandler, getLogger
import logging

from better_logger import BetterLogger

very_long_response={
  "forks_count": 9,
  "forks": 9,
  "stargazers_count": 80,
  "watchers_count": 80,
  "watchers": 80,
  "size": 108,
  "default_branch": "master",
  "open_issues_count": 0,
  "open_issues": 0,
}
def error_func():
    1/0#type:ignore because this is an example of error

def traceback_example():
    error_func()

logger = getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = StreamHandler()
logger.addHandler(stream_handler)

better_logger=BetterLogger(logger)
better_logger.debug('debug message')
better_logger.debug('debug message',header_text='debug with header')
better_logger.debug('debug message',header_text='debug with traceback',use_traceback=True)
better_logger.info(very_long_response,header_text='very_long_info')
better_logger.warning('warning message')
try:
    traceback_example()
except Exception as e:
    better_logger.error('do not divide by zero!',exception=e,header_text=e)
better_logger.critical('重大な問題が発生しました！',exception=Exception('重大な問題が発生しました！'),header_text='CRITICAL ERROR!')
