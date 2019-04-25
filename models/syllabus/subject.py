# -*- coding: utf-8 -*-

from odoo import models, fields


class Subject(models.Model):
    _name = "subject.subject"

    name = fields.Char(string="Subject", required=True)
    subject_uid = fields.Char(string="Code", required=True)

    _sql_constraints = [("name_subject_uid", "unique(name, subject_uid)", "Subject must be unique")]
