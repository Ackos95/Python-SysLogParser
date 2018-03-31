#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SysLogParser(object):
    # TODO: update methods to actually do something instead of simply reading all file lines

    class SysLogEntry(object):
        """
        Class representing base structure of syslog entry
        """

        def __init__(self, line_value):
            self.line_value = line_value

    @staticmethod
    def parse_rfc5424(syslog_lines):
        """
        Parses iterable of syslog file entry lines and creates iterable of `SysLogEntry` instances

        :param syslog_lines: Iterable containing all string lines of syslog file which should be parsed
        :return: Iterable containing syslog string lines converted into `SysLogEntry` objects
        """

        return map(lambda line: SysLogParser.SysLogEntry(line), syslog_lines)

    @staticmethod
    def parse_rfc3164(syslog_lines):
        """
        Parses iterable of syslog file entry lines and creates iterable of `SysLogEntry` instances

        :param syslog_lines: Iterable containing all string lines of syslog file which should be parsed
        :return: Iterable containing syslog string lines converted into `SysLogEntry` objects
        """

        return map(lambda line: SysLogParser.SysLogEntry(line), syslog_lines)

    @staticmethod
    def format_rfc5424(syslog_entries):
        """
        Formats iterable of `SysLogEntry` objects into iterable of syslog file lines

        :param syslog_entries: Iterable containing all `SysLogEntry` objects to be formatted
        :return: Iterable containing `SysLogEntry` objects formatted into syslog file line
        """

        return map(lambda entry: entry.line_value, syslog_entries)

    @staticmethod
    def format_rfc3164(syslog_entries):
        """
        Formats iterable of `SysLogEntry` objects into iterable of syslog file lines

        :param syslog_entries: Iterable containing all `SysLogEntry` objects to be formatted
        :return: Iterable containing `SysLogEntry` objects formatted into syslog file line
        """

        return map(lambda entry: entry.line_value, syslog_entries)
