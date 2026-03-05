from odoo.http import request
from odoo.addons.iap.tools import iap_tools
from odoo.exceptions import UserError, AccessError
from odoo import _

DEFAULT_OLG_ENDPOINT = 'https://olg.api.odoo.com'


def generate_text(self, prompt):
    try:
        IrConfigParameter = request.env['ir.config_parameter'].sudo()
        olg_api_endpoint = IrConfigParameter.get_param('web_editor.olg_api_endpoint', DEFAULT_OLG_ENDPOINT)
        database_id = IrConfigParameter.get_param('database.uuid')
        response = iap_tools.iap_jsonrpc(olg_api_endpoint + "/api/olg/1/chat", params={
            'prompt': prompt,
            'conversation_history': [],
            'database_id': database_id,
        }, timeout=30)
        if response['status'] == 'success':
            return response['content']
        elif response['status'] == 'error_prompt_too_long':
            raise UserError(_("Sorry, your prompt is too long. Try to say it in fewer words."))
        elif response['status'] == 'limit_call_reached':
            raise UserError(_("You have reached the maximum number of requests for this service. Try again later."))
        else:
            raise UserError(_("Sorry, we could not generate a response. Please try again later."))
    except AccessError:
        raise AccessError(_("Oops, it looks like our AI is unreachable!"))
