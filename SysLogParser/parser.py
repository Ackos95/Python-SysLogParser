#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SysLogParser(object):
    # TODO: update methods to actually do something instead of simply reading all file lines

    @staticmethod
    def parse_rfc5424(file_path):
        try:
            with open(file_path, 'r') as sys_log_file:
                data = list(sys_log_file.readlines())
            return data
        except IOError:
            return []

    @staticmethod
    def parse_rfc3164(file_path):
        try:
            with open(file_path, 'r') as sys_log_file:
                data = list(sys_log_file.readlines())
            return data
        except IOError:
            return []
