# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta


class DateCalendar(models.Model):
    _name = "arc.date.calendar"

    def date_array(self, from_date, till_date):
        from_obj = datetime.strptime(from_date, "%Y-%m-%d")
        till_obj = datetime.strptime(till_date, "%Y-%m-%d")

        total_days = (till_obj - from_obj).days + 1

        date_list = []
        for i in range(0, total_days):
            date_obj = from_obj + timedelta(days=i)
            date_list.append(date_obj.strftime("%Y-%m-%d"))

        return date_list
