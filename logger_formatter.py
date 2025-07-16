import logging


class LoggerSetup:
    """
    一个用于设置和获取日志记录器的类。
    """

    def __init__(self, name=__name__, level=logging.INFO):
        """
        初始化日志记录器并配置默认设置。

        :param name: 日志记录器的名称，默认为当前模块名。
        :param level: 日志记录级别，默认为 INFO。
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self):
        """
        配置控制台处理器并添加到日志记录器。
        """
        ch = logging.StreamHandler()
        ch.setLevel(self.logger.level)

        # 创建格式化器并添加到处理器
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)

        # 将处理器添加到日志记录器
        self.logger.addHandler(ch)

    def get_logger(self):
        """
        获取配置好的日志记录器。

        :return: 配置好的日志记录器
        """
        return self.logger


logger = LoggerSetup().get_logger()


def log_function_call(func):
    """
    一个装饰器函数，在函数执行前后记录日志。

    :param func: 被装饰的函数
    :return: 包装后的函数
    """

    def wrapper(*args, **kwargs):
        logger.info(f"Executing '{func.__name__}' with arguments {args} and keyword arguments {kwargs}.")
        result = func(*args, **kwargs)
        logger.info(f"'{func.__name__}' executed successfully.")
        return result

    return wrapper
