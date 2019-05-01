# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolStandard(models.Model):
    _name = "school.standard"
    _rec_name = "standard_id"

    academic_id = fields.Many2one(comodel_name="school.academic", string="Academic", required=True)
    image = fields.Binary(string="Image")
    standard_id = fields.Many2one(comodel_name="arc.standard", string="Standard", required=True)
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")

    total_staff = fields.Integer(string="Total Staff", compute="_get_total_staff")
    total_student = fields.Integer(string="Total Student", compute="_get_total_student")
    male_student = fields.Integer(string="Boys", compute="_get_male_student")
    female_student = fields.Integer(string="Girls", compute="_get_female_student")

    section_ids = fields.One2many(comodel_name="school.section", inverse_name="standard_id")

    @api.multi
    def _get_total_student(self):
        return 0

    @api.multi
    def _get_male_student(self):
        return 0

    @api.multi
    def _get_female_student(self):
        return 0

    @api.multi
    def _get_total_staff(self):
        return 0
