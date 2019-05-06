# -*- coding: utf-8 -*-

from odoo import models, fields, api


class QuestionPaper(models.Model):
    _name = "question.paper"

    name = fields.Char(string="Name", readonly=True)
    subject_id = fields.Many2one(comodel_name="arc.subject", string="Subject")
    syllabus_id = fields.Many2one(comodel_name="syllabus.subject", string="Syllabus")
    question_ids = fields.Many2many(comodel_name="question.bank", string="Question")
    prepared_by = fields.Many2one(comodel_name="arc.person", string="Prepared By")
    prepared_on = fields.Date(string="Prepared On")
    comment = fields.Text(string="Comment")

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(QuestionPaper, self).create(vals)
