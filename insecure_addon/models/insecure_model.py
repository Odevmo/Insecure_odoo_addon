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

    # 4.1 Direct ORM Bypass
    def raw_bypass(self):
        # Bypasses the ORM entirely (no injection risk here, but skips ACLs & business logic)
        self.env.cr.execute('SELECT id FROM insecure_model')
        return [row[0] for row in self.env.cr.fetchall()]

    # 4.2 SQL Injection Vulnerability
    def raw_injection(self, keyword):
        # Vulnerable: user input interpolated via % → SQL injection possible
        query = "SELECT * FROM insecure_model WHERE name = '%s'" % keyword
        self.env.cr.execute(query)
        return self.env.cr.fetchall()

    # 5. Unsafe eval
    @api.model
    def eval_input(self, expr):
        # dangerous eval of arbitrary string
        return eval(expr)
