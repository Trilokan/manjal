# -*- coding: utf-8 -*-

from odoo import models, fields, api

RESULT_INFO = [("pass", "Pass"), ("fail", "Fail")]


class SchoolMark(models.Model):
    _name = "school.mark"

    evaluation_id = fields.Many2one(comodel_name="school.evaluation", string="Evaluation")
    student_id = fields.Many2one(comodel_name="school.student", string="Student")
    total_marks = fields.Float(string="Total Marks", default=0.0, required=True)
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")
    result = fields.Selection(selection=RESULT_INFO, string="Result")
    comment = fields.Text(string="Comment")
