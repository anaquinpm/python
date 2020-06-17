g_var = 0                           # variable local al bloque
nl_var = 0                          # variable local al bloque
print(f"top level-> g_var: {g_var} nl_var: {nl_var}")

def test():
    nl_var = 2                      # variable local de la función
    print(f"in test-> g_var: {g_var} nl_var: {nl_var}")
    def inner_test():
        global g_var                # "global" referencia a la variable global.
        nonlocal nl_var             # "nonloacal" referencia la variable del bloque anterior.
        g_var = 1
        nl_var = 4
        print(f"in inner_test-> g_var: {g_var} nl_var: {nl_var}")

    inner_test()
    print(f"in test-> g_var: {g_var} nl_var: {nl_var}")

test()
print(f"top level-> g_var: {g_var} nl_var: {nl_var}")
