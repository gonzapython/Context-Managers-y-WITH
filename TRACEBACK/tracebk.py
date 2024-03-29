import sys, traceback

def funcion_primera():
    funcion_segunda()

def funcion_segunda():
    return tuple()[0]

try:
    funcion_primera()

except IndexError:
    exc_type, exc_value, exc_traceback = sys.exc_info()

    print("                    ")
    print("*** print_traceback:")
    print("--------------------")
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)

    print("                    ")
    print("*** print_exception:")
    print("--------------------")
    # exc_type below is ignored on 3.5 and later
    traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=2, file=sys.stdout)

    print("              ")
    print("*** print_exc:")
    print("--------------")
    traceback.print_exc(limit=2, file=sys.stdout)

    print("                                    ")
    print("*** format_exc, first and last line:")
    print("------------------------------------")
    formatted_lines = traceback.format_exc().splitlines()
    print(formatted_lines[0])
    print(formatted_lines[-1])

    print("                     ")
    print("*** format_exception:")
    print("---------------------")
    # exc_type below is ignored on 3.5 and later
    print(repr(traceback.format_exception(exc_type, exc_value,
                                          exc_traceback)))

    print("                      ")
    print("*** extract_traceback:")
    print("----------------------")
    print(repr(traceback.extract_tb(exc_traceback)))

    print("                     ")
    print("*** format_traceback:")
    print("---------------------")
    print(repr(traceback.format_tb(exc_traceback)))

    print("                        ")
    print("*** traceback_num_linea:", exc_traceback.tb_lineno)
    print("                        ")
