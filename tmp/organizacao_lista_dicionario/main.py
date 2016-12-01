
dados = (
        [1, "clienteA", 111, 'dado aleatorio'],
        [2, "clienteB", 222, 'dado aleatorio'],
        [3, "clienteC", 333, 'dado aleatorio'],
        [4, "clienteC", 111, 'dado aleatorio'],
        [5, "clienteB", 333, 'dado aleatorio'],
        [6, "clienteA", 222, 'dado aleatorio'],
        [7, "clienteB", 111, 'dado aleatorio'],
        [8, "clienteC", 222, 'dado aleatorio'],
        [9, "clienteA", 444, 'dado aleatorio'],
        )

novos = {i[1]:i[0] if 1==1 else i[1]:i[2] for i in dados}

print(novos)
