# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("confirmed", "Confirmed")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%m %H:%M:%S")


class SchoolAttendance(models.Model):
    _name = "school.attendance"

    date = fields.Date(string="Date", required=True, default=CURRENT_DATE)
    academic_id = fields.Many2one(comodel_name="school.academic", string="Academic")
    standard_id = fields.Many2one(comodel_name="school.standard", string="Standard")
    section_id = fields.Many2one(comodel_name="school.section", string="Section")
    teacher_id = fields.Many2one(comodel_name="arc.person", string="Teacher")
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", default="draft")
    comment = fields.Text(string="Comment")
    attendance_detail = fields.One2many(comodel_name="school.attendance.item", inverse_name="attendance_id")
    writter = fields.Text(string="Writter", track_visibility="always")
    report = fields.Html(string="Report", compute="_get_report")

    @api.multi
    def confirmed(self):
        writter = "Attendance for {0} - {1} confirmed by {2} on {3}".format(self.standard_id,
                                                                            self.section_id,
                                                                            self.teacher_id.name,
                                                                            CURRENT_INDIA)

        self.write({"progress": "confirmed", "writter": writter})

    @api.multi
    def trigger_item_detail(self):
        recs = self.section_id.student_ids

        item = []
        for rec in recs:
            item.append((0, 0, {"student_id": rec.id,
                                "attendance_id": self.id}))

        self.env["school.attendance.item"].create(item)

    @api.multi
    def _get_report(self):
        for rec in self:
            pass

        return True


class SchoolAttendanceItem(models.Model):
    _name = "school.attendance.item"

    student_id = fields.Many2one(comodel_name="school.student", string="Student")
    forenoon = fields.Boolean(string="Forenoon", default=True)
    afternoon = fields.Boolean(string="Afternoon", default=True)
    attendance_id = fields.Many2one(comodel_name="school.attendance", string="Attendance")
    progress = fields.Selection(selection=PROGRESS_INFO, related="attendance_id.progress")

