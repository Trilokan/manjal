# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

TRANSACT_TYPE = [("in", "In"), ("out", "Out")]
PROGRESS_INFO = [("draft", "Draft"), ("moved", "Moved")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class MaterialTransact(models.Model):
    _name = "material.transact"
    _inherit = "mail.thread"

    date = fields.Date(string="Date", default="", required=True)
    name = fields.Char(string="Name", readonly=True)
    person_id = fields.Many2one(comodel_name="arc.person", string="Person", required=True)
    order_id = fields.Many2one(comodel_name="arc.order", string="Order", required=True)
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", default="draft")
    transact_by = fields.Many2one(comodel_name="arc.person", string="Transact By")
    transact_on = fields.Date(string="Transact On")
    transact_type = fields.Selection(selection=TRANSACT_TYPE, string="Transact Type", required=True)
    transact_detail = fields.One2many(comodel_name="transact.detail", inverse_name="transact_id")
    comment = fields.Text(string="Comment")
    writter = fields.Text(string="Writter", track_visibility="always")
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")


class MaterialTransactDetail(models.Model):
    _name = "transact.detail"

    name = fields.Char(string="Name", readonly=True)
    product_id = fields.Many2one(comodel_name="arc.product", string="Product", required=True)
    uom_id = fields.Many2one(comodel_name="product.uom", string="UOM", related="product_id.uom_id")
    description = fields.Text(string="Description")
    request_quantity = fields.Float(string="Request Quantity", default=0.0, required=True)
    received_quantity = fields.Float(string="Received Quantity", default=0.0, required=True)
    quantity = fields.Float(string="Receiving Quantity", default=0.0, required=True)
    transact_id = fields.Many2one(comodel_name="material.transact", string="Material Transact")
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", related="transact_id.progress")
