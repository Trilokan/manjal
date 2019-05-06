# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Rank(models.TransientModel):
    _name = "school.rank"

    academic_id = fields.Many2one(comodel_name="school.academic", string="Academic")
    standard_id = fields.Many2one(comodel_name="school.standard", string="Standard")
    section_id = fields.Many2one(comodel_name="school.section", string="Section")
    student_ids = fields.Many2many(comodel_name="school.student", string="Student")
    rank = fields.Html(string="Rank")

