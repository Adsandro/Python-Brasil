def converterHoras (horario):
        if horario > 12.59 and horario < 24:
            horario = horario - 12
            print("São exatamente", float(horario), "AM")
        elif horario > 24:
            print("O horario informado esta incorreto")
        else:
            horario = horario
            print("São exatamente", float(horario), "PM")
h = input("informe o horario atual: ")
converterHoras(float(h))