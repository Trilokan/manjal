# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class Awards(models.Model):
    _name = "school.award"

    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    student_id = fields.Many2one(comodel_name="school.student", string="Student", required=True)
    standard_id = fields.Many2one(comodel_name="school.standard", string="Standard")
    section_id = fields.Many2one(comodel_name="school.section", string="Section")
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")
    comment = fields.Text(string="Comment")

