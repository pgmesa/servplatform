# + Integrantes del grupo: 
# -> Pablo García Mesa
# -> Santiago González Gómez
# -> Fernando Fernández Martín
 
# ------------------- MAIN (INICIO DE EJECUCION) ---------------------
# --------------------------------------------------------------------
# Este es un fichero fachada en el cual se ve de forma global el 
# flujo de ejecucion que sigue el programa sin entrar en detalles
# --------------------------------------------------------------------
# Los criterios de nivel de logger que va a seguir el programa son:
# --> Se usara:
# - logger.warning():
# cuando se necesite informar al usuario de algo importante
# - logger.error():
# cuando alguna accion no se haya podido completar por algun motivo
# - logger.critical():
# cuando un error impida la continuacion de la ejecucion del programa 
# --------------------------------------------------------------------
from dependencies.utils.decorators import timer
# --------------------------------------------------------------------
@timer
def main():
    logging.basicConfig(level=logging.NOTSET)
    main_logger = logging.getLogger(__name__)
    
    cli = Cli(get_main_cmd(), def_advanced_help=True)
    try:
        # Procesamos la linea de comandos (CmdLineError)
        args_processed = cli.process_cmdline(sys.argv)
        # Realizamos unas comprobaciones previas (ProgramError)
        program.check_dependencies()
        program.check_platform_updates()
        # Iniciamos el programa
        servplatform(**args_processed)
    except CmdLineError as clErr:
        main_logger.error(f" {clErr}"); exit(1)
    except ProgramError as err:
        main_logger.critical(err); exit(1)
    except KeyboardInterrupt:
        main_logger.warning(" Programa interrumpido"); exit(1)
    except Exception as err:
        err_msg = " Error inesperado en el programa (no controlado)"
        main_logger.critical(err_msg) 
        answer = input("¿Obtener traza completa?(y/n): ")
        if answer.lower() == "y":
            main_logger.exception(err)
        exit(1) 

# --------------------------------------------------------------------
if __name__ == "__main__":
    import sys
    import json
    import logging

    from dependencies.cli.cli import Cli, CmdLineError
    from program import program
    from program.program import ProgramError
    from commands.main_cmd import get_main_cmd, main as servplatform 
    from dependencies.cli.cli import Cli
    main()
# --------------------------------------------------------------------
