# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Journal(models.Model):
    _name = "arc.journal"

    name = fields.Char(string="Name")
    journal_uid = fields.Char(string="Code")

    _sql_constraints = [("name", "unique(name)", "Journal must be unique"),
                        ("journal_uid", "unique(journal_uid)", "Journal Code must be unique")]

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(Journal, self).create(vals)
