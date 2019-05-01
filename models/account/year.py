# -*- coding: utf-8 -*-

from odoo import models, fields


class ArcYear(models.Model):
    _name = "arc.year"

    name = fields.Char(string="Year", required=True)
    physical_year = fields.Char(string="Financial Year", required=True)
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)



