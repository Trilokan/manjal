# -*- coding: utf-8 -*-

from odoo import models, fields


class Academic(models.Model):
    _name = "academic.academic"

    name = fields.Char(string="Academic", required=True)

    _sql_constraints = [("name", "unique(name)", "Academic Year must be unique")]
