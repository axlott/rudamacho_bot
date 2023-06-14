from telebot.util import quick_markup

MARKUP_BIENVENIDA = quick_markup(
    {
        'Registrarse': {'callback_data': 'cb_logup'},
        'Ingresar': {'callback_data': 'cb_login'},
    }
)

MARKUP_LOGUP = (
    quick_markup(
        {
            'Volver': {'callback_data': 'vl1_volver'},
            'Continuar': {'callback_data': 'lu1_ok'},
        }
    ),
    quick_markup(
        {
            'Cancelar': {'callback_data': 'vl1_volver'},
            'Volver': {'callback_data': 'vl2_volver'},
        }
    ),
)
