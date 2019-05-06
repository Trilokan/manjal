# -*- coding:utf-8 -*-

from odoo import models, fields, api

ACTIVITY_TYPE = [("co_curricular", "Co-Curricular"), ("extra_curricular", "Extra-Curricular")]


class ActivityMaster(models.Model):
    _name = "activity.master"

    name = fields.Char(string="Name", required=True)
    activity_type = fields.Selection(selection=ACTIVITY_TYPE, string="Activity Type", required=True)
