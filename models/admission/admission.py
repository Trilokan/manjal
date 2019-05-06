# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("admitted", "Admitted"), ("transferred", "Transferred")]
RELATION_INFO = [('father', 'Father'),
                 ('mother', 'Mother'),
                 ('wife', 'Wife'),
                 ('brother', 'Brother'),
                 ('sister', 'Sister'),
                 ('uncle', 'Uncle'),
                 ('aunt', 'Aunt'),
                 ('grand_father', 'Grand Father'),
                 ('grand_mother', 'Grand Mother'),
                 ('son', 'Son'),
                 ('daughter', 'Daughter')]

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class StudentAdmission(models.Model):
    _name = "school.student"

    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    name = fields.Char(string="Name", readonly=True)
    image = fields.Binary(string="Image", readonly=True)
    student_id = fields.Many2one(comodel_name="arc.student", string="Student", required=True)
    student_uid = fields.Char(string="Student", related="student_id.student_uid")
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", default="draft")

    comment = fields.Text(string="Comment")
    writter = fields.Text(string="Writter", track_visibility="always")

    # Admission
    academic_id = fields.Many2one(comodel_name="school.academic", string="Academic", required=True)
    standard_id = fields.Many2one(comodel_name="school.standard", string="Standard", required=True)
    section_ids = fields.Many2many(comodel_name="school.section", string="Section")
    # is_account_approved_admission = fields.Boolean(string="Accounts Approved")

    # Transfer
    # is_class_teacher_approved_transfer = fields.Boolean(string="Class Teacher Approved")
    # is_account_approved_transfer = fields.Boolean(string="Accounts Approved")

    tc = fields.Html(string="Transfer Certificate", readonly=True)

    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")

    # Guardian Detail
    contact_person = fields.Char(string="Name")
    relation_type = fields.Selection(selection=RELATION_INFO, string="Relation", default="father")
    phone = fields.Char(string="Phone")
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="e-mail")
    address = fields.Text(string="Address")
    state_id = fields.Many2one(comodel_name="res.country.state", string="State")
    country_id = fields.Many2one(comodel_name="res.country", string="Country")

    @api.multi
    def trigger_admit(self):
        writter = "{0} admitted by {1} on {2}".format(self.student_id.name,
                                                      self.env.user.name,
                                                      CURRENT_INDIA)
        self.write({"progress": "admitted", "writter": writter})

    @api.multi
    def trigger_transfer(self):
        writter = "{0} transferred by {1} on {2}".format(self.student_id.name,
                                                         self.env.user.name,
                                                         CURRENT_INDIA)
        self.write({"progress": "transferred", "writter": writter})

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(StudentAdmission, self).create(vals)
