# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("confirmed", "Confirmed"), ("approved", "Approved")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class SchoolSyllabusItem(models.Model):
    _name = "syllabus.item"

    sequence = fields.Integer(string="Sequence", required=True)
    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Description")
    syllabus_id = fields.Many2one(comodel_name="school.syllabus", string="Syllabus")
    progress = fields.Selection(selection=PROGRESS_INFO, related="syllabus_id.progress")
    parent_id = fields.Many2one(comodel_name="syllabus.item", string="Syllabus")
    child_ids = fields.One2many(comodel_name="syllabus.item", inverse_name="parent_id")
    comment = fields.Char(string="Comment")

    question_bank_ids = fields.One2many(comodel_name="question.bank", inverse_name="syllabus_item_id")
