#!/usr/bin/python3.8
# coding=utf-8
"""
Icinga Summary
"""
import tableformatter as tf
from tableformatter import generate_table, FancyGrid, Column
from icinga2ve.api import get_object


columns = (Column('Check', attrib='check'),
           Column('Status', attrib='get_status'),
           Column('Output', attrib='output'))


class IcingaStatus(object):
    """Icinga Status Object"""
    def __init__(self, check: str, status: int, output: str):
        self.check = check
        self.status = status
        self.output = output

    def get_status(self):
        """Status is complex"""
        if self.status == 2:
            return 'Critical'
        elif self.status == 1:
            return 'Warning'
        elif self.status == 0:
            return 'OK'
        else:
            return 'Unknown'

    def get_color(self):
        """Status is complex"""
        if self.status == 2:
            return tf.TableColors.TEXT_COLOR_RED
        elif self.status == 1:
            return tf.TableColors.TEXT_COLOR_YELLOW
        elif self.status == 0:
            return tf.TableColors.TEXT_COLOR_GREEN
        else:
            return tf.TableColors.TEXT_COLOR_BLUE


def status_color(row_obj: IcingaStatus) -> dict:
    """Color rows."""
    return {tf.TableFormatter.ROW_OPT_TEXT_COLOR: row_obj.get_color()}


def main(host: str, basicauth: bool):
    services = get_object(object='services', basicauth=basicauth, host=host)
    rows = [
        IcingaStatus(service, data['state'], data['output'])
        for service, data in services.items()
    ]
    print(generate_table(rows, columns, grid_style=FancyGrid(), row_tagger=status_color))
