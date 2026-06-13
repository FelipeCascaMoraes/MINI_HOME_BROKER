saldo = 1000

print(f"Saldo inicial: R$ {saldo:.2f}")

carteira = {
    "PETR4": 0,
    "VALE3": 0,
    "ITUB4": 0,
    "BBDC4": 0,
    "BBAS3": 0,
}

acoes ={
    "PETR4": 10,
    "VALE3": 20,
    "ITUB4": 30,
    "BBDC4": 40,
    "BBAS3": 50,
}

def mostrar_carteira():
    print("=== CARTEIRA ===")
    print()
    print(f"Saldo R$:{saldo:.2f}")
    print()
    for ticker, quantidade in carteira.items():
        print(f"{ticker}: {quantidade}")
        print()

def mostrar_acoes():
    print("=== home broker ===")
    print()
    print(f"Saldo R$:{saldo:.2f}")
    print()
    for ticker, preco in acoes.items():
        print(f"{ticker}: R$ {preco:.2f}")

def comprar_acao():
    mostrar_acoes()
    global saldo
    global carteira
    escolha_acao = input("Escolha uma ação para comprar: ")
    quantidade = int(input("Quantidade: "))
    if escolha_acao not in acoes:
        print("Ação inválida")
        return
    custo = acoes[escolha_acao]* quantidade
    if custo <= saldo:
        saldo -= custo
        carteira[escolha_acao] += quantidade
        print("Parabéns pela compra!")
        mostrar_carteira()
        print()
    else:
        print("Saldo insuficiente para comprar a ação")

def vender_acao():
    mostrar_acoes()
    mostrar_carteira()
    global saldo
    global carteira
    escolha_venda = input("Escolha uma ação para vender: ")
    quantidade_venda = int(input("Quantida da Venda: "))
    if escolha_venda not in acoes:
        print("Escolha uma ação válida para venda!")
        return
    if quantidade_venda <=  carteira[escolha_venda]:
        valor_venda = acoes[escolha_venda] * quantidade_venda
        saldo += valor_venda
        print("Parabéns pela venda!")
        mostrar_carteira()
        print()
    else:
        print("Você não possui essa quantidade")


while True:
    print("1. Comprar ação")
    print("2. Vender ação")
    print("3. Ver carteira")
    print("4. Sair")
    print()

    escolha = int(input("escolha uma opção: "))
    if escolha == 1:
        comprar_acao()
    elif escolha == 2:
        vender_acao()
    elif escolha == 3:
        mostrar_carteira()
    elif escolha == 4:
        print("Você está saindo do Mini Home Broker...")
        break
    else:
        print("Opção inválida")
        print("Digite uma opção válida")
