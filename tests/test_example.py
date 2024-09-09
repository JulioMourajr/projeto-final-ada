import unittest
from unittest.mock import patch
from io import StringIO
import sys

# Supondo que a função coletar_informacoes_pet esteja no arquivo info_pet.py
from info_pet import coletar_informacoes_pet

class TestColetarInformacoesPet(unittest.TestCase):

    @patch('builtins.input', side_effect=['Bicho', '5', '10.5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_coletar_informacoes_pet_validas(self, mock_stdout, mock_input):
        coletar_informacoes_pet()
        output = mock_stdout.getvalue()
        self.assertIn("Nome: Bicho", output)
        self.assertIn("Idade: 5 anos", output)
        self.assertIn("Peso: 10.5 kg", output)

    @patch('builtins.input', side_effect=['Bicho', '-1', '5', '10.5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_coletar_informacoes_pet_idade_negativa(self, mock_stdout, mock_input):
        coletar_informacoes_pet()
        output = mock_stdout.getvalue()
        self.assertIn("A idade não pode ser negativa. Tente novamente.", output)
        self.assertIn("Nome: Bicho", output)
        self.assertIn("Idade: 5 anos", output)
        self.assertIn("Peso: 10.5 kg", output)

    @patch('builtins.input', side_effect=['Bicho', 'cinco', '5', '10.5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_coletar_informacoes_pet_idade_invalida(self, mock_stdout, mock_input):
        coletar_informacoes_pet()
        output = mock_stdout.getvalue()
        self.assertIn("Por favor, insira um número válido para a idade.", output)
        self.assertIn("Nome: Bicho", output)
        self.assertIn("Idade: 5 anos", output)
        self.assertIn("Peso: 10.5 kg", output)

    @patch('builtins.input', side_effect=['Bicho', '5', '-10.5', '10.5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_coletar_informacoes_pet_peso_negativo(self, mock_stdout, mock_input):
        coletar_informacoes_pet()
        output = mock_stdout.getvalue()
        self.assertIn("O peso não pode ser negativo. Tente novamente.", output)
        self.assertIn("Nome: Bicho", output)
        self.assertIn("Idade: 5 anos", output)
        self.assertIn("Peso: 10.5 kg", output)

    @patch('builtins.input', side_effect=['Bicho', '5', 'dez', '10.5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_coletar_informacoes_pet_peso_invalido(self, mock_stdout, mock_input):
        coletar_informacoes_pet()
        output = mock_stdout.getvalue()
        self.assertIn("Por favor, insira um número válido para o peso.", output)
        self.assertIn("Nome: Bicho", output)
        self.assertIn("Idade: 5 anos", output)
        self.assertIn("Peso: 10.5 kg", output)

if __name__ == '__main__':
    unittest.main()