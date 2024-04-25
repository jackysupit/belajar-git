# -*- coding: utf-8 -*-
from odoo import http
import json

class ApiCheck(http.Controller):
    ####--------------------------------------------------------------------------------------
    ## User
    ####--------------------------------------------------------------------------------------

    @http.route('/api/satu', methods=['GET'], auth='user', type='http', website=True, csrf=False)
    def api_satu(self,  **kw):
        data = {
            'status': True,
            'message': 'Hello, this is Api Check (http / user) Get 1. If you are reading this, it means you have succesfully accessing this API.',
            'parameters': {
                'notes': 'if you passed parameters, then they should appears below',
                'kw': kw,
            }
        }
        return json.dumps(data)
