# insecure_addon/models/insecure_model.py
from odoo import models, fields, api

class InsecureModel(models.Model):
    _name = 'insecure.model'
    _description = 'Insecure Model'

    name = fields.Char(string="Name")
    data = fields.Text(string="Data")

    # 1. Public method with no access check
    def do_unchecked_write(self):
        for rec in self:
            rec.write({'name': 'Hacked'})  # no check_group or sudo()

    # 2. Direct ORM Bypass (skips ACLs)
    def raw_bypass(self):
        self.env.cr.execute('SELECT id FROM insecure_model')
        return [row[0] for row in self.env.cr.fetchall()]

    # 3. SQL Injection Vulnerability
    def raw_injection(self, keyword):
        query = "SELECT * FROM insecure_model WHERE name = '%s'" % keyword
        self.env.cr.execute(query)
        return self.env.cr.fetchall()

    # 4. Unsafe eval
    @api.model
    def eval_input(self, expr):
        return eval(expr)

    # 5. Unsafe Attribute Access
    def unsafe_getattr(self, field_name):
        return getattr(self, field_name)

    # 6. Improper HTML Construction
    def unsafe_html_builder(self, user_input):
        return "<div>" + user_input + "</div>"

    # 7. Sanitization vs. Escaping Misuse
    def unsafe_sanitization(self, user_input):
        from odoo.tools import html_sanitize
        return html_sanitize(user_input)
