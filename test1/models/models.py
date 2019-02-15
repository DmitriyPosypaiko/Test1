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
class Puppers(models.Model):
    _name = 'puppers.puppers'
    name = fields.Char(string='Name', size= 256, track_visibility='onchange')
    year = fields.Integer(string='Year')
    gender = fields.Selection([('male', 'male'),('doggess', 'doggess')],
                                string='Gender')
    parents_id = fields.One2many(comodel_name='dog.dog',
                                inverse_name="pupper_id",
                                string="Parents")

class Owner(models.Model):
    _name = 'owner.owner'
    # firstname = fields.Char(string='firstname', size= 256, track_visibility='onchange')
    # lastname = fields.Char(string='lastname', size= 256, track_visibility='onchange')
    owner = fields.Many2one(comodel_name='res.partner', string='Owner')
    dog_id = fields.One2many(comodel_name='dog.dog', ondelete="cascade",
                            inverse_name="owner_id", string="Dog")
    date_start = fields.Date(string='Start date',
                            default=fields.Date.context_today,
                            track_visibility='onchange')
    date_end = fields.Date(string='End date',
                            default=fields.Date.context_today,
                            track_visibility='onchange')
    duration = fields.Integer(string='Duration',
                              compute='_compute_duration')
    info = fields.Char(string='Owner',track_visibility='onchange')

    @api.depends('date_start', 'date_end')
    def _compute_duration(self):
                if self.date_start and self.date_end:
                    start_date = fields.Datetime.from_string(self.date_start)
                    end_date = fields.Datetime.from_string(self.date_end)
                    self.duration = (end_date - start_date).days + 1

class Dog(models.Model):
    _name = 'dog.dog'
    _inherit = 'puppers.puppers'
    owner_id = fields.Many2one(comodel_name='owner.owner',string='Owner')
    pupper_id = fields.Many2one(comodel_name='puppers.puppers', string='Pupper')
# class Parents(models.Model):
#     _name = 'parents.parents'
#     _inherit = 'dog.dog'
#
#     pupper_id = fields.Many2one(comodel_name='puppers.puppers', string='Pupper')


    # puppies_ids = fields.Many2many(comodel_name='puppies.puppies',
    #                                 ondelete="cascade",
    #                                 string='Puppies')
