import asyncio
import time

from django.http import JsonResponse


async def contador(request):
    inicio = time.perf_counter()
    segundos = 0

    for _ in range(5):
        await asyncio.sleep(1)
        segundos += 1

    tempo_total = time.perf_counter() - inicio

    return JsonResponse({
        "mensagem": "Contagem finalizada!",
        "contador": segundos,
        "tempo_total": round(tempo_total, 2),
    })
