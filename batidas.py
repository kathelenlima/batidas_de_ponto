from datetime import datetime, timedelta

def ler_horario(mensagem):
    horario_str = input(mensagem)
    return datetime.strptime(horario_str, '%H:%M')

def format_duration(td):
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(abs(total_seconds), 3600)
    minutes, _ = divmod(remainder, 60)
    sign = "-" if total_seconds < 0 else ""
    return f"{sign}{hours:02}:{minutes:02}"

while True:
    print("\nDigite os horários das batidas no formato HH:MM")
    
    batida1 = ler_horario("Batida 1: ")
    batida2 = ler_horario("Batida 2: ")
    batida3 = ler_horario("Batida 3: ")
    batida4 = ler_horario("Batida 4: ")

    if batida4 < batida3:
        batida4 += timedelta(days=1)

    periodo1 = batida2 - batida1
    periodo2 = batida4 - batida3

    print("\nPeríodo entre batida 1 e 2:", format_duration(periodo1))
    print("Período entre batida 3 e 4:", format_duration(periodo2))

    teste = periodo1 + periodo2
    jornada = timedelta(hours=8, minutes=48)

    print("Jornada do dia: ", format_duration(teste))

    if teste > jornada:
        horas_extra = teste - jornada
        print(f"Hora extra: {format_duration(horas_extra)}")
    elif teste < jornada:
        horas_devidas = jornada - teste
        print(f"O funcionário ficou devendo: -{format_duration(horas_devidas)}")
    else:
        print("Não teve hora extra")

    continuar = input("\nDeseja continuar com outra avaliação? (sim/não): ").lower()

    if continuar != 'sim':
        break
