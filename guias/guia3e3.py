tarifadia = 12000
tarifanoche = 16000
semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
tarifadiadomingo = tarifadia + 2000
tarifanochedomingo = tarifanoche + 3000
empleados = {
    "Empleado 1": {
        "Lunes": "Nocturno",
        "Martes": "Nocturno",
        "Miércoles": "Nocturno",
        "Jueves": "Diurno",
        "Viernes": "Diurno",
        "Sábado": "",
        "Domingo": ""
    },
    "Empleado 2": {
        "Lunes": "",
        "Martes": "Nocturno",
        "Miércoles": "Nocturno",
        "Jueves": "Nocturno",
        "Viernes": "",
        "Sábado": "",
        "Domingo": "Diurno"
    },
    "Empleado 3": {
        "Lunes": "",
        "Martes": "",
        "Miércoles": "Diurno",
        "Jueves": "Diurno",
        "Viernes": "Diurno",
        "Sábado": "Nocturno",
        "Domingo": "Nocturno"
    }
}
for empleado, horario in empleados.items():
    pagosemanal = 0
    for dia, turno in horario.items():
        if turno == "Diurno":
            if dia == "Domingo":
                pagodia = tarifadiadomingo * 10
            else:
                pagodia = tarifadia * 10
        elif turno == "Nocturno":
            if dia == "Domingo":
                pagodia = tarifanochedomingo * 10
            else:
                pagodia = tarifanoche * 10
        else:
            pagodia = 0
        if turno != "":
            print(f"{empleado} trabaja {dia} en turno {turno}: Pago diario = {pagodia} CLP")
            pagosemanal += pagodia
    empleados[empleado]["pagosemanal"] = pagosemanal
    print(f"Total semanal de {empleado}: {pagosemanal} CLP\n")
for empleado, info in empleados.items():
    print(f"Empleado: {empleado}")
    print(f"  Pago semanal total: {info["pagosemanal"]} CLP\n")