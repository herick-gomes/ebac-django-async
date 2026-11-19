from unittest.mock import AsyncMock, patch

from django.test import TestCase
from django.urls import reverse


class ContadorTests(TestCase):

    @patch("core.views.asyncio.sleep", new_callable=AsyncMock)
    def test_contador_assincrono(self, mock_sleep):
        response = self.client.get(reverse("contador"))

        self.assertEqual(response.status_code, 200)

        dados = response.json()

        self.assertEqual(dados["contador"], 5)
        self.assertEqual(
            dados["mensagem"],
            "Contagem finalizada!"
        )
        self.assertGreaterEqual(dados["tempo_total"], 0)
        self.assertEqual(mock_sleep.await_count, 5)
