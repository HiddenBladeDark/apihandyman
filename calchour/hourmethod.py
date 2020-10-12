
import numpy as np
from datetime import datetime, timedelta


# sacar total de horas
def hourjobtol(start,end):
    return abs(int((start-end).total_seconds())) / 3600

# metodo para las horas laboradas
def hourjobnorm(start,end):
    print(start,' - ' ,end)
    # inicializamos variable tol
    tol = 0
     # dia de la semana sea menor a 5 por ser lunes a sabado 
    if start.weekday() <= 5:
        print(start.hour, ' - ', end.hour)
        # la hora sea mayor o igual a 7 y menor a 20
        if start.hour >= 7 and end.hour <= 20:
            # calculo de las horas que hay entre el rango de entrada
            tol += abs(int((start-end).total_seconds())) / 3600
            print(tol,'horas totales    ')
            return tol
        # total de horas mayor igual a 7
        if start.hour >= 7:
            # asignamos valor a horas de inicio
            hourstart = start.hour            
            # mientras la hora de inicio sea menor a 20
            while hourstart < 20:
                # contamos las horas de inicio hasta que llegue a 20
                hourstart += 1
                # horas transcurridas
                tol += 1
            print(tol,'horas trabajadas luego de las 20')
            # retornamos
            return tol
        # total de horas sea menor igual a 20
        if end.hour <= 20:
            # asignamos valor a las horas de inicio a 7
            hourstart = 7
            # mientras las horas de inicio sea menor a la hora final laborada
            while hourstart < end.hour:
                # contamos las horas de inicio hasta que llegue a la hora final
                hourstart += 1
                # horas transcurridas
                tol += 1
            print(tol,'horas trabajadas antes de las 20')
            # retornamos hora total
            return tol
        if start.hour <= 7 and end.hour >= 20:
            hourstart = 7
            while hourstart < 20:
                hourstart += 1
                tol += 1
            return tol
        else:
            return tol
    return tol


# horas nocturnas
def hourjobnoct(start,end):
    print(start,' - ' ,end)
    # inicializamos variable tol
    tol = 0
    # dia de la semana sea menor a 5 por ser lunes a sabado 
    if start.weekday() <= 5:
        # print(start.hour, ' - ', end.hour)
        # horas laborales
        if start.hour >= 20 and end.hour <= 23:
            tol += abs(int((start-end).total_seconds())) / 3600
            # print(tol,'horas totales    ')
            # return tol 
            # print(tol,'hora luego de las 20')
            return tol
        if start.hour >= 0 and end.hour <= 7:
            tol += abs(int((start-end).total_seconds())) / 3600
            # print(tol,'horas totales    ')
            # return tol 
            # print(tol,'hora luego de las 20')
            return tol    
        if start.hour >= 0:
            hourstart = start.hour
            ehourend = end.hour
            while hourstart < 7:
                hourstart += 1
                tol += 1
        if end.hour >= 20 and end.hour <= 23:
            print('entro 1?')
            hourstart = 20
            ehourend = end.hour
            while hourstart < ehourend:
                hourstart += 1
                tol += 1              
        else:
            return tol
        return tol 
    else:
        return tol


def hourjobdom(start,end):
    # dia de la semana sea menor a 6 por ser lunes a sabado 
    print(start.weekday)
    if start.weekday() == 6:
        return abs(int((start-end).total_seconds())) / 3600 
    else:
        return 0