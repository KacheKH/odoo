# -*- coding: utf-8 -*-

from openerp import models, fields


class petro(models.Model):
    _name = 'petro.producto'

    codbod = fields.Char('Codigo Bodega')
    descinv = fields.Char('Descripcion SubInventario')
    grupmat = fields.Char('Grupo Material')
    codart = fields.Char('Codigo Articulo')
    cantstock = fields.Float('Cantidad Inventario Stock')
    umed = fields.Char('Unidad Medida')
    descart = fields.Text('Descripcion Articulo')

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
