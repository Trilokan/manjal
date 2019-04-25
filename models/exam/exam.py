# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("confirmed", "Confirmed"), ("done", "Done")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class SchoolExam(models.Model):
    _name = "school.exam"
    _inherit = "mail.thread"

    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    name = fields.Char(string="Name", readonly=True)
    section_id = fields.Many2one(comodel_name="school.section", string="Section", required=True)
    standard_id = fields.Many2one(comodel_name="school.standard", string="Standard", required=True)
    academic_id = fields.Many2one(comodel_name="school.academic", string="Academic", required=True)
    teacher_id = fields.Many2one(comodel_name="arc.person", string="Teacher", required=True)
    type_id = fields.Many2one(comodel_name="exam.type", string="Exam", required=True)
    syllabus_ids = fields.Many2many(comodel_name="school.syllabus", string="Syllabus", required=True)
    description = fields.Html(string="Description")
    question_ids = fields.Many2many(comodel_name="question.bank", string="Question")
    total_marks = fields.Float(string="Total Marks", required=True, default=0.0)
    comment = fields.Text(string="Comment")
    writter = fields.Text(string="Writter", track_visibility="always")

    @api.multi
    def trigger_confirm(self):
        writter = "Test confirm by {0} on {1}".format(self.env.user.name, CURRENT_INDIA)
        self.write({"progress": "confirmed", "writter": writter})

    @api.multi
    def trigger_done(self):
        writter = "Test done by {0} on {1}".format(self.env.user.name, CURRENT_INDIA)
        self.write({"progress": "done", "writter": writter})

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(SchoolExam, self).create(vals)
