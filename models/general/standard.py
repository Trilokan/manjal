# -*- coding: utf-8 -*-

from odoo import models, fields


class Standard(models.Model):
    _name = "standard.standard"

    name = fields.Char(string="Standard", required=True)

    _sql_constraints = [("name", "unique(name)", "Standard must be unique")]
