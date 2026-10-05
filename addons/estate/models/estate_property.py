from odoo import fields, models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'
    
    name = fields.Char(string="Nama", required=True)
    description = fields.Text(string="Deskripsi")
    postcode = fields.Char(string="Kode Pos")
    date_availability = fields.Date(string="Tanggal Tersedia",copy=False, default=lambda self: fields.Date.today() + relativedelta(months=3))
    expected_price = fields.Float(string="Harga Harapan", required=True)
    selling_price = fields.Float(string="Harga Jual", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Kamar Tidur", default=2)
    living_area = fields.Integer(string="Luas Bangunan")
    facades = fields.Integer(string="Fasad")
    garage = fields.Boolean(string="Garasi")
    garden = fields.Boolean(string="Taman")
    garden_area = fields.Integer(string="Luas Taman")
    garden_orientation = fields.Selection(
        selection=[
            ('south', 'Selatan'),
            ('east', 'Timur'),
            ('north', 'Utara'),
            ('west', 'Barat'),
        ],
        string="Orientasi Taman",
        default='north'
    )
    active = fields.Boolean(string="Aktif", default=False)
    status = fields.Selection(
        selection=[
            ('new', 'Baru'),
            ('offer_received', 'Penawaran Diterima'),
            ('offer_accepted', 'Penawaran Diterima'),
            ('sold', 'Terjual'),
            ('canceled', 'Dibatalkan'),
        ],
        string="Status",
        required=True,
        copy=False,
        default='new'
    )
    property_type_id = fields.Many2one("estate.property.type", string="Tipe Properti")
    salesperson_id = fields.Many2one("res.users", string="Pramuniaga", index=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Pembeli", index=True, copy=False)
    tags_ids = fields.Many2many("estate.property.tags", string="Label Properti")