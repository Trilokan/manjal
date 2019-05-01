# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolSection(models.Model):
    _name = "school.section"
    _rec_name = "section_id"

    image = fields.Binary(string="Image")
    academic_id = fields.Many2one(comodel_name="school.academic", string="Academic", required=True)
    standard_id = fields.Many2one(comodel_name="school.standard", string="Standard", required=True)
    section_id = fields.Many2one(comodel_name="arc.section", string="Section", required=True)
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")

    total_staff = fields.Integer(string="Total Staff", compute="_get_total_staff")
    total_student = fields.Integer(string="Total Student", compute="_get_total_student")
    male_student = fields.Integer(string="Boys", compute="_get_male_student")
    female_student = fields.Integer(string="Girls", compute="_get_female_student")

    supervisor_id = fields.Many2one(comodel_name="arc.person", string="Class Teacher")
    leader_id = fields.Many2one(comodel_name="school.student", string="Class Leader")

    # student_ids = fields.Many2many(comodel_name="school.student", string="Student")
    # subject_ids = fields.One2many(comodel_name="school.subject", inverse_name="section_id")
    # test_ids = fields.One2many(comodel_name="school.test", inverse_name="section_id")
    # exam_ids = fields.One2many(comodel_name="school.exam", inverse_name="section_id")
    # mark_ids = fields.One2many(comodel_name="school.exam", inverse_name="section_id")
    # rank_ids = fields.One2many(comodel_name="school.exam", inverse_name="section_id")
    # homework_ids = fields.One2many(comodel_name="school.homework", inverse_name="section_id")
    # attendance_ids = fields.One2many(comodel_name="school.attendance", inverse_name="section_id")
    # time_table_ids = fields.One2many(comodel_name="school.time.table", inverse_name="section_id")

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
