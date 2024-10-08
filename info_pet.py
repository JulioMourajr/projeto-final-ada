# Função para coletar informações sobre o pet
def coletar_informacoes_pet(input_func=input):
    print("Por favor, insira as informações sobre seu pet.")

    # Coleta do nome do pet
    nome = input_func("Nome do pet: ")

    # Coleta da idade do pet, garantindo que seja um número inteiro
    while True:
        try:
            idade = int(input_func("Idade do pet (em anos): "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

    # Coleta do peso do pet, garantindo que seja um número flutuante
    while True:
        try:
            peso = float(input_func("Peso do pet (em kg): "))
            if peso < 0:
                print("O peso não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para o peso.")

    # Exibindo as informações coletadas
    print("\nInformações do pet:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Peso: {peso} kg")

if __name__ == "__main__":
    coletar_informacoes_pet()
    

