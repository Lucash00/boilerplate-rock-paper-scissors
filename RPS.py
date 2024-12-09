def player(prev_play, opponent_history=[], play_order={}):
    # Si no hay jugada previa, asigna un valor por defecto (R).
    if not prev_play:
        prev_play = 'R'

    # Añadimos la jugada previa del oponente al historial de jugadas.
    opponent_history.append(prev_play)
    
    # Inicializamos la predicción con 'P' (Papel) por defecto.
    prediccion = 'P'

    # Si el historial de jugadas del oponente tiene más de 4 jugadas, se busca patrones.
    if len(opponent_history) > 4:
        # Obtenemos las últimas 5 jugadas del oponente y las unimos en un string.
        ultimos_5 = "".join(opponent_history[-5:])
        
        # Registramos las últimas 5 jugadas en play_order, sumando 1 si ya existía el patrón.
        play_order[ultimos_5] = play_order.get(ultimos_5, 0) + 1
        
        # Generamos las jugadas potenciales basadas en las últimas 4 jugadas del oponente
        # combinadas con las 3 posibles jugadas siguientes ('R', 'P', 'S').
        jugada_potencial = [
            "".join([*opponent_history[-4:], v]) 
            for v in ['R', 'P', 'S']
        ]
        
        # Filtramos los patrones registrados en play_order que coincidan con las jugadas potenciales.
        patrones = {
            k: play_order[k]
            for k in jugada_potencial if k in play_order
        }

        # Si se han encontrado patrones registrados, predice la siguiente jugada.
        if patrones:
            # Seleccionamos el patrón más frecuente y tomamos la última jugada del patrón.
            prediccion = max(patrones, key=patrones.get)[-1:]

    # Definimos un diccionario con la respuesta ideal a cada jugada del oponente.
    counter_play = {'P': 'S', 'R': 'P', 'S': 'R'}

    # Retornamos la jugada que contrarresta la predicción del oponente.
    return counter_play[prediccion]
