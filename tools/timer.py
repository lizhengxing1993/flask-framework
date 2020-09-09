# -*- coding: utf8 -*-
import datetime
import time
import calendar


class TimeManager(object):
    """时间转换工具"""

    @staticmethod
    def timestamp_to_str(timestamp, fmt="%Y-%m-%d %H:%M:%S"):
        """13位转字符串"""
        if isinstance(timestamp, int) or isinstance(timestamp, float):
            if len(str(int(timestamp))) >= 12:
                timestamp = float(timestamp / 1000)
            fmt_time = time.strftime(fmt, time.localtime(timestamp))
            return fmt_time
        else:
            return TimeManager.now(is_str=True)

    @staticmethod
    def str_to_timestamp(time_str, digit=13):
        """转时间戳,默认13位"""
        timestamp = (
            int(time.mktime(time.strptime(time_str, "%Y-%m-%d %H:%M:%S"))) * 1000
            if digit == 13
            else int(time.mktime(time.strptime(time_str, "%Y-%m-%d %H:%M:%S")))
        )
        return timestamp

    @staticmethod
    def convert_str(time_str, fmt_from="%Y-%m-%d %H:%M:%S", fmt_to="%Y-%m-%d %H_%M_%S"):
        """时间字符串的格式转换"""
        return datetime.datetime.strptime(time_str, fmt_from).strftime(fmt_to)

    @staticmethod
    def now(is_str=False, digit=13, format="%Y-%m-%d %H:%M:%S"):
        """获取当前的时间"""
        now_time = datetime.datetime.now()
        time_str = now_time.strftime(format)
        timestamp = (
            int(round(time.mktime(now_time.timetuple()) * 1000))
            if digit == 13
            else int(round(time.mktime(now_time.timetuple())))
        )
        return time_str if is_str else timestamp

    @staticmethod
    def last_24_hour(is_str=False, digit=13, days=1, now=None):
        """获取过去n天"""
        if now is None:
            now = datetime.datetime.now()
        if isinstance(now, str):
            now = datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
        if isinstance(now, int):
            now = (
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(now / 1000)))
                if len(str(now)) == 13
                else time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
            )
            now = datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
        yesterday = now - datetime.timedelta(days=days)
        time_str = yesterday.strftime("%Y-%m-%d %H:%M:%S")
        timestamp = (
            int(time.mktime(yesterday.timetuple()) * 1000)
            if digit == 13
            else int(time.mktime(yesterday.timetuple()))
        )
        return time_str if is_str else timestamp

    @staticmethod
    def past_time(unit, num, is_str=False, now_time=None):
        if now_time is None:
            now_time = datetime.datetime.now()
        if unit == "seconds":
            past_time = now_time - datetime.timedelta(seconds=num)
        elif unit == "days":
            past_time = now_time - datetime.timedelta(days=num)
        elif unit == "minutes":
            past_time = now_time - datetime.timedelta(minutes=num)
        elif unit == "hours":
            past_time = now_time - datetime.timedelta(hours=num)
        else:
            raise NotImplementedError
        time_str = past_time.strftime("%Y-%m-%d %H:%M:%S")
        timestamp = int(round(time.mktime(past_time.timetuple()) * 1000))
        return time_str if is_str else timestamp

    @staticmethod
    def get_current_timestamp():
        return int(round(time.time() * 1000))

    @staticmethod
    def timestamp_to_datetime(timestamp):
        return datetime.datetime.fromtimestamp(timestamp / 1000)

    @staticmethod
    def split_time(time_str):
        year = month = day = hour = minute = second = 0
        if "-" in time_str:
            year, month, day = time_str.split(" ")[0].split("-")
            hour, minute, second = time_str.split(" ")[1].split(":")
        else:
            if time_str.count(":") == 2:
                hour, minute, second = time_str.split(":")
            else:
                hour, minute = time_str.split(":")
        return int(year), int(month), int(day), int(hour), int(minute), int(second)

    @staticmethod
    def month_first_day(next_month=False):
        now_date = datetime.date.today()
        first_day = datetime.date(now_date.year, now_date.month, 1)
        if next_month:
            days_num = calendar.monthrange(first_day.year, first_day.month)[1]
            return first_day + datetime.timedelta(days=days_num)
        else:
            return first_day

    @staticmethod
    def month_last_day(next_month=False):
        month_first_day = TimeManager.month_first_day(next_month)
        month_days = calendar.monthrange(month_first_day.year, month_first_day.month)[1]
        month_last_day = month_first_day + datetime.timedelta(days=month_days - 1)
        return month_last_day

    @staticmethod
    def utcstr_to_str(utcstr, format="%Y-%m-%dT%H:%M:%S.%f+0800"):
        """
            处理utc类型的时间字符串
        :param utcstr: utc时间字符串
        :param format: utc格式
        :return:
        """
        utc_time = datetime.datetime.strptime(utcstr, format)
        local_str = utc_time.strftime("%Y-%m-%d %H:%M:%S")
        return local_str
