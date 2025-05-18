# insecure_addon/controllers/main.py
from odoo import http
from odoo.http import request

class InsecureController(http.Controller):

    @http.route('/insecure/xss', auth='public', methods=['GET'], csrf=False)
    def xss_demo(self, **kwargs):
        user_input = kwargs.get('input', '')
        # store raw input to show later
        record = request.env['insecure.model'].sudo().create({
            'name': 'XSS Demo',
            'data': user_input,
        })
        return request.render('insecure_addon.insecure_addon_template', {
            'record': record
        })

    @http.route('/insecure/sqli', auth='public', methods=['GET'], csrf=False)
    def sqli_demo(self, **kwargs):
        login = kwargs.get('login', '')
        # vulnerable SQL injection
        results = request.env['insecure.model'].sudo().raw_injection(login)
        return request.make_response(
            "<pre>%s</pre>" % results,
            headers=[('Content-Type', 'text/html')],
        )
