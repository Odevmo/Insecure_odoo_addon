# insecure_addon/controllers/main.py
from odoo import http
from odoo.http import request


class InsecureController(http.Controller):

    @http.route('/insecure/xss', auth='public', methods=['GET'], csrf=False)
    def xss_demo(self, **kwargs):
        # Example: fetch latest record
        record = request.env['insecure.model'].sudo().search([], limit=1, order='id desc')

        # ✅ Real-world pattern: devs use query parameters to fetch records.
        #
        # ❌ Real flaw: This allows enumeration or exposure of records without permission checks.
        # Or optionally fetch by ID: /insecure/xss?id=3
        record_id = kwargs.get('id')
        if record_id:
            # ✅ Common in real modules: Devs often use sudo() in controllers to "avoid permission errors."
            #
            # ❌ Security risk: It completely bypasses ACLs and record rules, exposing sensitive data to public or unauthorized users.
            record = request.env['insecure.model'].sudo().browse(int(record_id))

        if not record:
            return request.not_found()

        # The controller blindly passes a record whose data field was written from untrusted input (the backend form).
        #
        # If the associated template uses t-raw, the data is injected into HTML as-is — classic Stored XSS.
        #
        # ❗ This is especially dangerous when combined with the auth='public' flag.

        return request.render('insecure_addon.insecure_addon_template', {
            'record': record
        })

    @http.route('/insecure/sqli', auth='public', methods=['GET'], csrf=False)
    def sqli_demo(self, **kwargs):
        login = kwargs.get('login', '')
        results = request.env['insecure.model'].sudo().raw_injection(login)
        result_str = "<br>".join(str(row) for row in results)
        return request.make_response(
            f"<h3>Results for input: {login}</h3><pre>{result_str}</pre>",
            headers=[('Content-Type', 'text/html')],
        )
