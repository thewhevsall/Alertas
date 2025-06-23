import telegram
import asyncio
from datetime import datetime

TOKEN = "8078511575:AAGZ1D1Br4bV-WS9_xRwFFwUTyFRZ6Vxtp8"
CHAT_ID = "-1002775415060"

# Diccionario para traducir días y meses al español
dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

ahora = datetime.now()
dia_semana = dias_semana[ahora.weekday()]
dia = ahora.day
mes = meses[ahora.month - 1]
hora = ahora.strftime("%H:%M:%S")

MENSAJE = f"🚨 Esta es una alerta de prueba.\nGenerada el {dia_semana} {dia} de {mes} a las {hora}"

bot = telegram.Bot(TOKEN)

async def enviar_mensaje(chat_id, mensaje):
    try:
        await bot.send_message(chat_id=chat_id, text=mensaje)
    except Exception:
        pass

asyncio.run(enviar_mensaje(CHAT_ID, MENSAJE))