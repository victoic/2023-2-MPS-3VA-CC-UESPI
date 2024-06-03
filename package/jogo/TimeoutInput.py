import msvcrt
import time, sys

class TimeoutExpired(Exception):
    pass

def input_com_tempo(texto, segundos, timer=time.monotonic):
    sys.stdout.write(texto)
    sys.stdout.flush()
    tempo_fim = timer() + segundos
    resultado = []
    while timer() < tempo_fim:
        if msvcrt.kbhit():
            resultado.append(msvcrt.getwche())
            if resultado[-1] == '\r':
                return ''.join(resultado[:-1])
        time.sleep(0.04)
    raise TimeoutExpired