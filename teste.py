import unittest
from unittest.mock import patch
from io import StringIO
from info_pet import coletar_informacoes_pet

class TestInfoPet(unittest.TestCase):

    def test_coletar_informacoes_pet_valid(self):
        # Testa se recebe corretamente as informações.
        with patch('builtins.input', side_effect=['Bolinha', '5', '3']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                coletar_informacoes_pet()
                expected_output = (
                    "Por favor, insira as informações sobre seu pet.\n"
                    "Informações do pet:\n"
                    "Nome: Bolinha\n"
                    "Idade: 5 anos\n"
                    "Peso: 3.0 kg\n"
                )
                self.assertEqual(fake_output.getvalue(), expected_output)

    def test_coletar_informacoes_pet_negative_age(self):
        # Testa para quando inserir valor negativo para idade
        with patch('builtins.input', side_effect=['Bolinha', '-5', '3', '2']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                coletar_informacoes_pet()
                expected_output = (
                    "Por favor, insira as informações sobre seu pet.\n"
                    "A idade não pode ser negativa. Tente novamente.\n"
                    "Informações do pet:\n"
                    "Nome: Bolinha\n"
                    "Idade: 2 anos\n"
                    "Peso: 3.0 kg\n"
                )
                self.assertEqual(fake_output.getvalue(), expected_output)

    def test_coletar_informacoes_pet_invalid_age(self):
        # Testa se recebe a idade corretamente
        with patch('builtins.input', side_effect=['Bolinha', 'abc', '5', '3']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                coletar_informacoes_pet()
                expected_output = (
                    "Por favor, insira as informações sobre seu pet.\n"
                    "Por favor, insira um número válido para a idade.\n"
                    "Informações do pet:\n"
                    "Nome: Bolinha\n"
                    "Idade: 5 anos\n"
                    "Peso: 3.0 kg\n"
                )
                self.assertEqual(fake_output.getvalue(), expected_output)

    def test_coletar_informacoes_pet_negative_weight(self):
        # Testa para ver se peso é negativo
        with patch('builtins.input', side_effect=['Bolinha', '5', '-3', '2']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                coletar_informacoes_pet()
                expected_output = (
                    "Por favor, insira as informações sobre seu pet.\n"
                    "O peso não pode ser negativo. Tente novamente.\n"
                    "Informações do pet:\n"
                    "Nome: Bolinha\n"
                    "Idade: 5 anos\n"
                    "Peso: 2.0 kg\n"
                )
                self.assertEqual(fake_output.getvalue(), expected_output)

    def test_coletar_informacoes_pet_invalid_weight(self):
        # Esse teste é para saber se essa função trata o peso dela corretamente
        with patch('builtins.input', side_effect=['Bolinha', '5', 'abc', '3']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                coletar_informacoes_pet()
                expected_output = (
                    "Por favor, insira as informações sobre seu pet.\n"
                    "Por favor, insira um número válido para o peso.\n"
                    "Informações do pet:\n"
                    "Nome: Bolinha\n"
                    "Idade: 5 anos\n"
                    "Peso: 3.0 kg\n"
                )
                self.assertEqual(fake_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
