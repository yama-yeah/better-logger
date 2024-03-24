# better-logger
BetterLogger is a simple and powerful logging package that makes it easy to display logs.  
It runs on python 3.8 or higher and can be used in the same way as Logging.
<img width="1031" alt="Screenshot 2024-03-25 at 2 10 38" src="https://github.com/yama-yeah/better-logger/assets/82094614/a767ae94-7488-4187-8bcc-22bc42cbe859">

## How to Install
```
pip install better-loggers
```

## Easy to use!
BetterLogger creates beautiful logs easily by writing.  
For detailed source code, please click [here](https://github.com/yama-yeah/better-logger/blob/main/example/example.py).
```python
from logging import StreamHandler, getLogger
import logging

from better_logger import BetterLogger

~~~~~~~~

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
```

