# -*- coding: utf-8 -*-

from odoo import models, fields, api


class QuestionBank(models.Model):
    _name = "question.bank"

    question = fields.Text(string="Question", required=True)
    answer = fields.Html(string="Answer", required=True)
    total_mark = fields.Float(string="Marks", required=True, default=0.0)
    comment = fields.Text(string="Comment")
    syllabus_item_id = fields.Many2one(comodel_name="syllabus.item", string="Syllabus")
    is_objective = fields.Boolean(string="Objective Type")
    option_ids = fields.One2many(comodel_name="question.bank.option", inverse_name="question_bank_id")


class QuestionBankOption(models.Model):
    _name = "question.bank.option"

    sequence = fields.Char(string="Sequence")
    answer = fields.Text(string="Answer")
    question_bank_id = fields.Many2one(comodel_name="question.bank", string="Question")

