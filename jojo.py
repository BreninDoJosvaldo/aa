saldo_bancario = 2000
movimentacao = int(input('retirar digite 1, depositar digite 2, sair digite 0'))
while movimentacao != 0:
    if movimentacao == 1:
        retirar = int(input())
        saldo_bancario = saldo_bancario - retirar
        print ( saldo_bancario )
        movimentacao = int(input('retirar digite 1, depositar digite 2, sair digite 0'))
    if movimentacao == 2:
        depositar =int(input())
        saldo_bancario = saldo_bancario + depositar
        print( saldo_bancario )
        movimentacao = int(input('retirar digite 1, depositar digite 2, sair digite 0'))
else:
    print("obrigado")
