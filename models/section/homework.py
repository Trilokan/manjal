# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("confirmed", "Confirmed")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class Homework(models.Model):
    _name = "school.homework"
    _inherit = "mail.thread"

    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    name = fields.Char(string="Name", readonly=True)
    academic_id = fields.Many2one(comodel_name="school.academic", string="Academic")
    standard_id = fields.Many2one(comodel_name="school.standard", string="Standard")
    section_id = fields.Many2one(comodel_name="school.section", string="Section", required=True)
    home_work = fields.Html(string="Home Work")
    comment = fields.Text(string="Comment")
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", default="draft")
    writter = fields.Text(string="Writter", track_visibility="always")

    @api.multi
    def trigger_confirm(self):
        writter = "Homework confirm by {0} on {1}".format(self.env.user.name, CURRENT_INDIA)
        self.write({"progress": "confirmed", "writter": writter})

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        section_id = self.env["school.section"].search([("academic_id", "=", vals["academic_id"])])
        vals["academic_id"] = section_id.academic_id.id
        vals["standard_id"] = section_id.standard_id.id
        return super(Homework, self).create(vals)
