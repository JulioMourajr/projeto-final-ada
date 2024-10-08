import unittest
from unittest.mock import patch
from io import StringIO
from info_pet import coletar_informacoes_pet

class TestColetarInformacoesPet(unittest.TestCase):

    @patch('builtins.input', side_effect=['Bicho', '5', '10.5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_coletar_informacoes_pet_validas(self, mock_stdout, mock_input):
        coletar_informacoes_pet(input_func=mock_input) 
        output = mock_stdout.getvalue() 
        self.assertIn("Nome: Bicho", output)
        self.assertIn("Idade: 5 anos", output)
        self.assertIn("Peso: 10.5 kg", output)

    @patch('builtins.input', side_effect=['Bicho', '-1', '5', 'dez', '10.5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_coletar_informacoes_pet_idade_peso_invalidos(self, mock_stdout, mock_input):
        coletar_informacoes_pet(input_func=mock_input)  
        output = mock_stdout.getvalue()
        self.assertIn("A idade não pode ser negativa. Tente novamente.", output)
        self.assertIn("Por favor, insira um número válido para o peso.", output)
        self.assertIn("Nome: Bicho", output)
        self.assertIn("Idade: 5 anos", output)
        self.assertIn("Peso: 10.5 kg", output)

if __name__ == '__main__':
    unittest.main()