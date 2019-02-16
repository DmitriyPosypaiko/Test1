# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class test1(models.Model):
#     _name = 'test1.test1'
#
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class Partner(models.Model):
    _inherit = 'res.partner'

    pets_ids = fields.One2many('test1.dog', string='Pets', inverse_name='owner_id')


class Dog(models.Model):
    _name = 'test1.dog'

    name = fields.Char(string='Name', size=256, track_visibility='onchange', required='True')
    mather_id = fields.Many2one('test1.dog', 'mather', domain=[('sex', '=', 'female')])
    father_id = fields.Many2one('test1.dog', 'father', domain=[('sex', '=', 'male')])
    owner_id = fields.Many2one('res.partner', 'Owner', required='True')
    bersday = fields.Date('Bersday', required='True')
    image = fields.Binary('Image', attachment=True)
    # pupper_id = fields.Many2one(comodel_name='test1.puppers', string='Pupper')
    sex = fields.Selection([('male', 'male'),('female', 'female')], string='Sex', required='True')



    # @api.depends('date_start', 'date_end')
    # def _compute_duration(self):
    #             if self.date_start and self.date_end:
    #                 start_date = fields.Datetime.from_string(self.date_start)
    #                 end_date = fields.Datetime.from_string(self.date_end)
    #                 self.duration = (end_date - start_date).days + 1

# class Parents(models.Model):
#     _name = 'parents.parents'
#     _inherit = 'dog.dog'
#
#     pupper_id = fields.Many2one(comodel_name='puppers.puppers', string='Pupper')

# class Puppers(models.Model):
#     _name = 'test1.puppers'
#     name = fields.Char(string='Name', size= 256, track_visibility='onchange')
#     year = fields.Integer(string='Year')
#     gender = fields.Selection([('male', 'male'),('doggess', 'doggess')],
#     string='Gender')
#     parents_id = fields.One2many(comodel_name='test1.dog',
#     inverse_name="pupper_id",
#     string="Parents")

    # puppies_ids = fields.Many2many(comodel_name='puppies.puppies',
    #                                 ondelete="cascade",
    #                                 string='Puppies')
