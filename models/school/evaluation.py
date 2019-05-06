# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolEvaluation(models.Model):
    _name = "school.evaluation"

    date = ""
    name = ""
    academic_id = ""
    standard_id = ""
    section_id = ""
    subject_id = ""
    syllabus_ids = ""
    mark_ids = ""
    progress = ""
    eval_type = ""
