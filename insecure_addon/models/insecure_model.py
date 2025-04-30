from odoo import models, fields, api

class InsecureModel(models.Model):
    _name = 'insecure.model'
    _description = 'Insecure Model'

    name = fields.Char(string="Name")
    data = fields.Text(string="Data")

    # 3. Public method with no access check
    def do_unchecked_write(self):
        # This writes every record to have name = "Hacked"
        for rec in self:
            rec.write({'name': 'Hacked'})  # no check_group or sudo()

    # 4. Unsafe SQL
    def raw_sql(self, keyword):
        # vulnerable to SQL injection
        self.env.cr.execute("SELECT * FROM insecure_model WHERE name = '%s'" % keyword)
        return self.env.cr.fetchall()

    # 5. Unsafe eval
    @api.model
    def eval_input(self, expr):
        # dangerous eval of arbitrary string
        return eval(expr)
