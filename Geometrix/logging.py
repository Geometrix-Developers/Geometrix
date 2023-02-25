import os
import datetime


class Logger:
    """
    Logger Class - logs events

    :param log_time: whether timestamps should be added to logs
    :param log_user: whether the user should be logged
    """

    def __init__(self, log_time=False, log_user=False, log_file=False):
        """
        Creating logger object

        :param log_time: whether timestamps should be added to logs
        :param log_user: whether the user should be logged
        """
        self.log_time = log_time
        self.log_user = log_user

    def build_log_pre_msg(self):
        """
        build_log_pre_msg - function to create a pre-message for a log

        :return: pre-message of the log
        """
        msg = ["Log"]

        if self.log_time:
            msg.append(f" - {datetime.datetime.utcnow()}")
        if self.log_user:
            msg.append(f" - {os.getlogin()}")

        return str("".join(msg))

    def log(self, message):
        """
        log function - create a log in the Log file

        :param message: event to log
        :return: nothing
        """
        path = os.path.dirname(os.path.realpath(__file__))
        f = open("Log", "a")
        f.write(f"{self.build_log_pre_msg()}: {message}. \n")
        f.close()

    @staticmethod
    def no_pre_msg_log(message):
        """
        no_pre_msg_log function - function to add a log without a pre-message in the Log file

        :param message: event to log
        :return: nothing
        """
        path = os.path.dirname(os.path.realpath(__file__))
        f = open("Log", "a")
        f.write(f"{message}. \n")
        f.close()
