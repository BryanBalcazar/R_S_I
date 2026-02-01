from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SuscripcionISP(models.Model):
    _name = 'modulo_isp.suscripcion'
    _description = 'Suscripciones de Internet'
    _inherit = ['mail.thread', 'mail.activity.mixin'] # Para tener chat de seguimiento

    name = fields.Char(string='Referencia', required=True, copy=False, readonly=True, default=lambda self: _('Nuevo'))
    cliente_id = fields.Many2one('res.partner', string='Cliente', required=True)
    
    # Conexión con lo que hicimos en el inventario
    plan_id = fields.Many2one('product.product', string='Plan/Variante', domain=[('type', '=', 'service')], required=True)
    tipo_servicio = fields.Selection(related='plan_id.attribute_line_ids.attribute_id.name', string='Tecnología') # Relacionado al atributo
    
    # Lo que pediste de pagos
    termino_pago_id = fields.Many2one('account.payment.term', string='Plan de Pago', required=True)
    factura_id = fields.Many2one('account.move', string='Última Factura', readonly=True)
    
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('activo', 'Activo'),
        ('mora', 'En Mora'),
        ('suspendido', 'Suspendido'),
        ('cancelado', 'Cancelado')
    ], default='borrador', tracking=True)

    fecha_inicio = fields.Date(string='Fecha de Inicio', default=fields.Date.today)
    proxima_factura = fields.Date(string='Próxima Fecha de Cobro')

    # Secuencia SN001 automática
    @api.model
    def create(self, vals):
        if vals.get('name', _('Nuevo')) == _('Nuevo'):
            vals['name'] = self.env['ir.sequence'].next_by_code('modulo_isp.suscripcion') or _('Nuevo')
        return super(SuscripcionISP, self).create(vals)

    # Función profesional para crear la factura conectada
    def action_crear_factura(self):
        for rec in self:
            if not rec.plan_id:
                raise UserError("Debe seleccionar un plan de internet.")
            
            # Crear la factura (FN)
            factura = self.env['account.move'].create({
                'move_type': 'out_invoice',
                'partner_id': rec.cliente_id.id,
                'invoice_payment_term_id': rec.termino_pago_id.id,
                'invoice_origin': rec.name, # Aquí conecta SN con FN
                'invoice_line_ids': [(0, 0, {
                    'product_id': rec.plan_id.id,
                    'name': f"Servicio de Internet: {rec.plan_id.display_name}",
                    'quantity': 1,
                    'price_unit': rec.plan_id.list_price,
                })],
            })
            rec.factura_id = factura.id
            rec.estado = 'activo'
            return {
                'name': 'Factura Generada',
                'view_mode': 'form',
                'res_model': 'account.move',
                'res_id': factura.id,
                'type': 'ir.actions.act_window',
            }