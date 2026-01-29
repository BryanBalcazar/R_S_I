from odoo import models, fields, api

class SuscripcionISP(models.Model):
    _name = 'modulo_isp.suscripcion'
    _description = 'Suscripciones de Internet'

    name = fields.Char(string='Referencia de Suscripción', required=True)
    cliente_id = fields.Many2one('res.partner', string='Cliente', required=True)
    tipo_servicio = fields.Selection([
        ('fibra', 'Fibra Óptica'),
        ('radio', 'Radio Enlace')
    ], string='Tipo de Servicio', default='fibra')
    
    plan_id = fields.Many2one('product.product', string='Plan de Internet', domain=[('type', '=', 'service')])
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('activo', 'Activo'),
        ('suspendido', 'Suspendido'),
        ('cancelado', 'Cancelado')
    ], default='borrador')

    # Campo para el ANS (SLA)
    fecha_inicio = fields.Date(string='Fecha de Inicio', default=fields.Date.today)
    horas_respuesta_ans = fields.Integer(string='Tiempo de Respuesta ANS (Horas)', default=4)

class TicketsDaños(models.Model):
    _name = 'modulo_isp.ticket'
    _description = 'Tickets de Soporte'

    name = fields.Char(string='ID de Daño', required=True)
    suscripcion_id = fields.Many2one('modulo_isp.suscripcion', string='Suscripción Afectada')
    descripcion = fields.Text(string='Descripción del Daño')
    intensidad_daño = fields.Selection([
        ('baja', 'Baja - Navegación Lenta'),
        ('media', 'Media - Intermitencia'),
        ('alta', 'Alta - Sin Servicio')
    ], string='Nivel de Intensidad')