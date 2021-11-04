from odoo import models, fields, api
from odoo.exceptions import ValidationError


class VehicleFleet(models.Model):
    _name = 'vehicle.fleet'
    _description = 'Vehicle Fleet'

    name = fields.Char(
        string='Domain',
        required=True
    )
    purchase_date = fields.Date(
        string='Purchase date',
        required=True
    )
    kilometer = fields.Float(
        string='Kilometers',
        required=True
    )
    original_price = fields.Float(
        string='Original price'
    )
    actual_price = fields.Float(
        string='Actual price'
    )
    qty_service = fields.Integer(
        string='Number of services',
        compute='compute_service'
    )

    @api.constrains('original_price', 'kilometer')
    def check_values(self):
        if self.original_price <= 0:
            raise ValidationError('The original price cannot be negative.')
        if self.kilometer <= 0:
            raise ValidationError('The kilometers cannot be negative.')

    @api.onchange('kilometer')
    def onchange_service(self):
        for vehicle in self:
            if vehicle.original_price and vehicle.kilometer:
                # vehicle.actual_price =

    @api.depends('original_price', 'kilometer')
    def compute_service(self):
        for vehicle in self:
            #diff = (date.today().year - date_purchase.year) * 12 + (date.today().month  - date_purchase.month )
            #if (vehicle.purchase_date - date.today()).months
