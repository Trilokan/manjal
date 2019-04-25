# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

DAY = [("monday", "Monday"),
       ("tuesday", "Tuesday"),
       ("wednesday", "Wednesday"),
       ("thursday", "Thursday"),
       ("friday", "Friday"),
       ("saturday", "Saturday"),
       ("sunday", "Sunday")]
PROGRESS_INFO = [("draft", "Draft"), ("confirmed", "Confirmed")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class SchoolTimetable(models.Model):
    _name = "school.timetable"
    _inherit = "mail.thread"

    academic_id = fields.Many2one(comodel_name="school.academic", string="Academic", required=True)
    standard_id = fields.Many2one(comodel_name="school.standard", string="Standard", required=True)
    section_id = fields.Many2one(comodel_name="school.section", string="Section", required=True)
    day = fields.Selection(selection=DAY, string="Day", required=True)
    first_period = fields.Many2one(comodel_name="school.syllabus", string="I Period")
    second_period = fields.Many2one(comodel_name="school.syllabus", string="II Period")
    third_period = fields.Many2one(comodel_name="school.syllabus", string="III Period")

    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress")
    writter = fields.Text(string="Writter", track_visibility="always")

    @api.multi
    def trigger_confirm(self):
        writter = "Time Table confirmed by {0} on {1}".format(self.env.user.name, CURRENT_INDIA)
        self.write({"progress": "confirmed", "writter": writter})

    @api.constrains("first_period")
    def check_period_duplicate(self):
        pass
