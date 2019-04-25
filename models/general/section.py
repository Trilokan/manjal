# -*- coding: utf-8 -*-

from odoo import models, fields


class Section(models.Model):
    _name = "section.section"

    name = fields.Char(string="Section", required=True)

    _sql_constraints = [("name", "unique(name)", "Section must be unique")]
