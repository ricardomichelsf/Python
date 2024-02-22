def voto(nasci):
    from datetime import date
    ano = date.today().year
    idade = ano - nasci
    if idade < 16:
        return f"Com {idade} anos: NÂO VOTA"
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"

print('--'*20)
nasceu = int(input("Digite o ano de nascimento: "))
voto(nasceu)
