from odoo import fields, models

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'
    
    name = fields.Char(string="Nama", required=True)
    description = fields.Text(string="Deskripsi")
    postcode = fields.Char(string="Kode Pos")
    date_availability = fields.Date(string="Tanggal Tersedia")
    expected_price = fields.Float(string="Harga Harapan", required=True)
    selling_price = fields.Float(string="Harga Jual")
    bedrooms = fields.Integer(string="Kamar Tidur")
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
        string="Orientasi Taman"
    )