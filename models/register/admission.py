# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("admitted", "Admitted")]
RELATION_TYPE = [("father", "Father"), ("mother", "Mother")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class StudentAdmission(models.Model):
    _name = "school.student"

    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    name = fields.Char(string="Name", readonly=True)
    student_id = fields.Many2one(comodel_name="arc.student", string="Student", required=True)
    academic_id = fields.Many2one(comodel_name="school.academic", string="Academic", required=True)
    standard_id = fields.Many2one(comodel_name="school.standard", string="Standard", required=True)
    section_ids = fields.Many2many(comodel_name="school.section", string="Section")
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", default="draft")
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")
    comment = fields.Text(string="Comment")
    writter = fields.Text(string="Writter", track_visibility="always")

    # Guardian Detail
    contact_person = fields.Char(string="Name")
    relation_type = fields.Selection(selection=RELATION_TYPE, string="Relation", default="father")
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
        self.write({"progress": "admit", "writter": writter})

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(Admission, self).create(vals)
