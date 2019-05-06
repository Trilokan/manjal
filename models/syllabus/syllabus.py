# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("confirmed", "Confirmed"), ("approved", "Approved")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class SchoolSyllabus(models.Model):
    _name = "school.syllabus"

    syllabus_id = fields.Many2one(comodel_name="syllabus.syllabus", string="Syllabus", required=True)
    section_id = fields.Many2one(comodel_name="school.section", string="Section", required=True)
    subject_id = fields.Many2one(comodel_name="arc.subject", string="Subject", required=True)
    teacher_id = fields.Many2one(comodel_name="arc.person", string="Teacher", required=True)
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")
    comment = fields.Text(string="Comment")


class SyllabusSyllabus(models.Model):
    _name = "syllabus.syllabus"

    standard_id = fields.Many2one(comodel_name="arc.standard", string="Standard", required=True)
    subject_id = fields.Many2one(comodel_name="arc.subject", string="Subject", required=True)
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", default="draft")
    approved_on = fields.Date(string="Approved On", readonly=True)
    approved_by = fields.Date(string="Approved By", readonly=True)
    syllabus_ids = fields.One2many(comodel_name="syllabus.subject", inverse_name="syllabus_id")
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")
    comment = fields.Text(string="Comment")
    writter = fields.Text(string="Writter", track_visibility="always")


class SyllabusSubject(models.Model):
    _name = "syllabus.subject"

    sequence = fields.Integer(string="Sequence", required=True)
    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Description")
    syllabus_id = fields.Many2one(comodel_name="syllabus.syllabus", string="Syllabus")
    progress = fields.Selection(selection=PROGRESS_INFO, related="syllabus_id.progress")
    parent_id = fields.Many2one(comodel_name="syllabus.subject", string="Syllabus")
    child_ids = fields.One2many(comodel_name="syllabus.subject", inverse_name="parent_id")
    comment = fields.Char(string="Comment")

    question_bank_ids = fields.One2many(comodel_name="question.bank", inverse_name="syllabus_id")
