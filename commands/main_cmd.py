
import json
import logging

# Imports para definicion del comando
from dependencies.cli.aux_classes import Command, Flag, Option
from .deploy_cmd.deploy import get_deploy_cmd, deploy
from .start_cmd.start import get_start_cmd, start
from .stop_cmd.stop import get_stop_cmd, stop
from .pause_cmd.pause import get_pause_cmd, pause
from .delete_cmd.delete import get_delete_cmd, delete
from .destroy_cmd.destroy import get_destroy_cmd, destroy
from .servs_cmd.servs import get_servs_cmd, servs
from .client_cmd.client import get_client_cmd, client
from .loadbal_cmd.loadbal import get_loadbal_cmd, loadbal
from .database_cmd.database import get_database_cmd, database
from .repo_cmd.repo import get_repo_cmd, repo
from .show_cmd.show import get_show_cmd, show
from .term_cmd.term import get_term_cmd, term
from .publish_cmd.publish import get_publish_cmd, publish
from .reused_definitions import def_reused_definitions
# Imports para la funcion asociada al comando
from program.platform import platform

def get_main_cmd() -> Command:
    def_reused_definitions()
    # MAIN COMMAND:
    main_msg = """Despliega y controla una plataforma de servidores"""
    main = Command(
        "main.py", description=main_msg
    )
    # DEPLOY +++++++++++++++++++++
    deploy_cmd = get_deploy_cmd(); main.nest_cmd(deploy_cmd)
    # START ++++++++++++++++++++++
    start_cmd = get_start_cmd(); main.nest_cmd(start_cmd)
    # STOP +++++++++++++++++++++++
    stop_cmd = get_stop_cmd(); main.nest_cmd(stop_cmd)
    # PAUSE ++++++++++++++++++++++
    pause_cmd = get_pause_cmd(); main.nest_cmd(pause_cmd)
    # DELETE +++++++++++++++++++++
    delete_cmd = get_delete_cmd(); main.nest_cmd(delete_cmd)
    # DESTROY ++++++++++++++++++++
    destroy_cmd = get_destroy_cmd(); main.nest_cmd(destroy_cmd)
    # SERVS ++++++++++++++++++++++
    servs_cmd = get_servs_cmd(); main.nest_cmd(servs_cmd)
    # CLIENT +++++++++++++++++++++
    client_cmd = get_client_cmd(); main.nest_cmd(client_cmd)
    # LOADBAL ++++++++++++++++++++
    lb_cmd = get_loadbal_cmd(); main.nest_cmd(lb_cmd)
    # DATABASE +++++++++++++++++++
    db_cmd = get_database_cmd(); main.nest_cmd(db_cmd)
    # REPO +++++++++++++++++++++++
    repo_cmd = get_repo_cmd(); main.nest_cmd(repo_cmd)
    # SHOW +++++++++++++++++++++++
    show_cmd = get_show_cmd(); main.nest_cmd(show_cmd)
    # TERM +++++++++++++++++++++++
    term_cmd = get_term_cmd(); main.nest_cmd(term_cmd)
    # PUBLISH ++++++++++++++++++++
    publish_cmd = get_publish_cmd(); main.nest_cmd(publish_cmd)
    
    # ---------------- Flags
    msg = """ 
    'warning mode', only shows warning and error msgs during 
    execution
    """
    verbosity = Flag(
        "-w", description=msg,notcompat_withflags=["-d"]
    )
    main.add_flag(verbosity)
    # -----------------------------
    msg = """ 
    'debug mode' option for debugging. Shows debug msgs during
    execution
    """
    debugging = Flag(
        "-d", description=msg, notcompat_withflags=["-w"]
    )
    main.add_flag(debugging)
    # -----------------------------
    msg = """ 
    'quiet mode', doesn't show any msg during execution (only 
    when an error occurs)
    """
    quiet = Flag(
        "-q", description=msg, notcompat_withflags=["-w","-d"],
    )
    main.add_flag(quiet)
    # -----------------------------
    msg = """ 
    executes the code sequencially instead of concurrently
    """
    sequential_execution = Flag("-s", description=msg)
    main.add_flag(sequential_execution)   

    return main

# -------------------------------------------------------------------- 
# -------------------------------------------------------------------- 
main_logger = logging.getLogger(__name__)
def main(args:list=[], options:dict={}, flags:list=[], nested_cmds:dict={}):
    # Configuramos el nivel de logger del programa
    """!!!IMPORTANTE¡¡¡:
    Para que esta forma de configurar el root_logger funcione es 
    necesario que los imports se hagan de la forma: 
    ---> from module.loquesea.algo import ese_algo
    ya que hacer 'import modulo.esemodulo' parece que es muy distinto
    a la forma anterior y al interpretar el programa (antes de ejecutar)
    se guarda la info del logger del otro fichero importado en ese 
    momento (previo a la configuracion del root_logger en esta funcion) 
    y no se hace en el momento de la ejecucion como con la forma 'from'"""
    if "-d" in flags:
        logLvl = logging.DEBUG
    elif "-w" in flags:
        logLvl = logging.WARNING
    elif "-q" in flags:
        logLvl = logging.ERROR
    else:
        logLvl = logging.INFO
    root_logger = logging.getLogger()
    root_logger.setLevel(logLvl)
    # Iniciamos el programa    
    main_logger.info(" Programa iniciado")
    # Informamos de parametros pasados al programa/comando principal
    nested_cmd_json = json.dumps(nested_cmds, indent=4, sort_keys=True)
    msg = (f" Parametros introducidos:\nargs={args}, options={options}, " + 
            f"flags={flags}\n{nested_cmd_json}")
    main_logger.debug(msg)
    # Miramos el comando introducido y ejecutamos la orden
    if "deploy" in nested_cmds:
        cmd_info = nested_cmds.pop("deploy")
        deploy(**cmd_info)
    elif "start" in nested_cmds:
        cmd_info = nested_cmds.pop("start")
        start(**cmd_info)
    elif "stop" in nested_cmds:
        cmd_info = nested_cmds.pop("stop")
        stop(**cmd_info)
    elif "pause" in nested_cmds: 
        cmd_info = nested_cmds.pop("pause")
        pause(**cmd_info)
    elif "delete" in nested_cmds:
        cmd_info = nested_cmds.pop("delete")
        delete(**cmd_info)
    elif "destroy" in nested_cmds:
        cmd_info = nested_cmds.pop("destroy")
        destroy(**cmd_info)
    elif "servs" in nested_cmds:
        cmd_info = nested_cmds.pop("servs")
        servs(**cmd_info)
    elif "client" in nested_cmds:
        cmd_info = nested_cmds.pop("client")
        client(**cmd_info)
    elif "loadbal" in nested_cmds:
        cmd_info = nested_cmds.pop("loadbal")
        loadbal(**cmd_info)
    elif "database" in nested_cmds:
        cmd_info = nested_cmds.pop("database")
        database(**cmd_info)
    elif "repo" in nested_cmds:
        cmd_info = nested_cmds.pop("repo")
        repo(**cmd_info)
    elif "show" in nested_cmds:
        cmd_info = nested_cmds.pop("show")
        show(**cmd_info)
    elif "term" in nested_cmds:
        cmd_info = nested_cmds.pop("term")
        term(**cmd_info)
    elif "publish" in nested_cmds:
        cmd_info = nested_cmds.pop("publish")
        publish(**cmd_info)
    # Para finalizar actualizamos la plataforma
    platform.update_conexions()
    main_logger.info(" Programa finalizado")