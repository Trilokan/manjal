# -*- coding:utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

ACTIVITY_TYPE = [("co_curricular", "Co-Curricular"), ("extra_curricular", "Extra-Curricular"), ("event", "Event")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class Activity(models.Model):
    _name = "school.activity"

    academics_id = fields.Many2one(comodel_name="school.academic", string="Academics")
    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    name = fields.Char(string="Name", readonly=True)
    activity_type = fields.Selection(selection=ACTIVITY_TYPE, string="Activity Type", required=True)
    activity_type_id = fields.Many2one(comodel_name="activity.type", string="Activity", required=True)
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")
    participants_ids = fields.One2many(comodel_name="activity.participants", inverse_name="activity_id", string="Participants")
    activity_detail = fields.Html(string="Activity Detail")
    supervisor_ids = fields.Many2many(comodel_name="arc.person", string="In-Charge")
    comment = fields.Text(string="Comment")

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(Activity, self).create(vals)


class ActivityParticipants(models.Model):
    _name = "activity.participants"

    student_id = fields.Many2one(comodel_name="school.student", string="Student", required=True)
    standard_id = fields.Many2one(comodel_name="school.standard", string="Standard")
    section_id = fields.Many2one(comodel_name="school.section", string="Section")
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")
    comment = fields.Text(string="Comment")
    activity_id = fields.Many2one(comodel_name="school.activity", string="Activity")


class ActivityType(models.Model):
    _name = "activity.type"

    activity_type = fields.Selection(selection=ACTIVITY_TYPE, string="Activity Type", required=True)
    name = fields.Char(string="Activity", required=True)
