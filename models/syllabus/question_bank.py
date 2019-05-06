# -*- coding: utf-8 -*-

from odoo import models, fields, api


class QuestionBank(models.Model):
    _name = "question.bank"

    syllabus_id = fields.Many2one(comodel_name="syllabus.subject", string="Syllabus")
    is_objective = fields.Boolean(string="Objective Type")
    total_mark = fields.Float(string="Marks", required=True, default=0.0)
    question = fields.Html(string="Question", required=True)
    option_ids = fields.One2many(comodel_name="question.bank.option", inverse_name="question_bank_id")
    answer = fields.Html(string="Answer", required=True)
    comment = fields.Text(string="Comment")


class QuestionBankOption(models.Model):
    _name = "question.bank.option"

    sequence = fields.Char(string="S.No")
    option = fields.Text(string="Option")
    question_bank_id = fields.Many2one(comodel_name="question.bank", string="Question")

