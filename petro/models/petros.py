# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Producto(models.Model):
    _name = 'petro.producto'

    codbod = fields.Char('Código Bodega')
    descinv = fields.Char('Descripción SubInventario')
    grupmat = fields.Char('Grupo Material')
    codart = fields.Char('Código Articulo')
    cantstock = fields.Integer('Cantidad Inventario Stock')
    umed = fields.Char('Unidad Medida')
    name = fields.Text('Descripcion Articulo')
    cnew = fields.Char('Código Nuevo')
    desp = fields.Char('Descripción Español')
    ding = fields.Char('Descripción Ingles')
    img = fields.Binary('Imagen del producto')
    subgrupo_id = fields.Many2one('petro.subgrupo', string='Subgrupo')


class Clase(models.Model):
    _name = 'petro.clase'

    codclase = fields.Char('Código Clase')
    name = fields.Char('Nombre')
    desclase = fields.Text('Descripción de la Clase')


class Grupo(models.Model):
    _name = 'petro.grupo'

    codgrupo = fields.Char('Codigo Grupo')
    name = fields.Char('Nombre')
    clase_id = fields.Many2one('petro.clase', string='Clase')


class Subgrupo(models.Model):
    _name = 'petro.subgrupo'

    codsubg = fields.Char('Código Subgrupo')
    name = fields.Char('Clase')
    grupo_id = fields.Many2one('petro.grupo', string='Grupo')
