# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("confirmed", "Confirmed"), ("approved", "Approved")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class SchoolSyllabus(models.Model):
    _name = "school.syllabus"

    standard_id = fields.Many2one(comodel_name="school.standard", string="Standard", required=True)
    subject_id = fields.Many2one(comodel_name="subject.subject", string="Subject", required=True)
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", default="draft")
    approved_on = fields.Date(string="Approved On", readonly=True)
    approved_by = fields.Date(string="Approved By", readonly=True)
    item_ids = fields.One2many(comodel_name="syllabus.item", inverse_name="syllabus_id")
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")
    comment = fields.Text(string="Comment")
    writter = fields.Text(string="Writter", track_visibility="always")
