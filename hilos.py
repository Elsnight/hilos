
import threading  #importamos la libreria
  
NUMERO_HILOS = 3  #asiganmos una constante para saber cuantos hilos deseamos

class Threaded_worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        threadName = threading.currentThread().getName()
        print("hola, soy un hilo %s" % threadName)

print('Iniciando %d Hilos...' % NUMERO_HILOS)#mensaje de inicio
for i in range(NUMERO_HILOS): #corremos con un for 
    td = Threaded_worker()
    td.start()