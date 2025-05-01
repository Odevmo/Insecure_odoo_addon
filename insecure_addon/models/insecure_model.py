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

    # 6. Unsafe Attribute Access (getattr/setattr vulnerability)
    def unsafe_getattr(self, field_name):
        # This is unsafe because it directly uses user input to access fields
        value = getattr(self, field_name)  # Unchecked access
        return value

    # 7. Improper HTML Construction (unsafe string concatenation)
    def unsafe_html_builder(self, user_input):
        html_content = "<div>" + user_input + "</div>"  # Unsafe concatenation
        return html_content

    # 8. Sanitization vs. Escaping Misuse
    def unsafe_sanitization(self, user_input):
        # This is unsafe because we are not escaping user input before sanitizing it
        from odoo.tools import html_sanitize
        sanitized_input = html_sanitize(user_input)  # Misused sanitization
        return sanitized_input

