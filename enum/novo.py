

class Carro:

    def __init__ (self):
        self.status = enumerate(['reservado', 'sem_reserva', 'emergencia'])


if __name__ == "__main__":

    palio = Carro()

    print type(palio.status)
