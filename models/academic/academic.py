# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolAcademic(models.Model):
    _name = "school.academic"

    academic_id = fields.Many2one(comodel_name="academic.academic", string="Academic", required=True)
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")

    total_student = fields.Integer(string="Total Student", compute="_get_total_student")
    male_student = fields.Integer(string="Boys", compute="_get_male_student")
    female_student = fields.Integer(string="Girls", compute="_get_female_student")

    total_staff = fields.Integer(string="Total Staff", compute="_get_total_staff")
    male_staff = fields.Integer(string="Male", compute="_get_male_staff")
    female_staff = fields.Integer(string="Female", compute="_get_female_staff")

    standard_ids = fields.One2many(comodel_name="school.standard", inverse_name="academic_id")

    _sql_constraints = [("academic_id", "unique(academic_id)", "Academic Year must be unique")]

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

    @api.multi
    def _get_male_staff(self):
        return 0

    @api.multi
    def _get_female_staff(self):
        return 0
