
import logging

# Imports para definicion del comando
from dependencies.cli.aux_classes import Command, Flag, Option
from ...reused_definitions import reused_opts, reused_flags
# Imports para la funcion asociada al comando
from program.platform.machines import client
from ...delete_cmd.delete import delete

def get_rm_cmd():
    msg = """removes the client"""
    rm = Command("rm", description=msg)
    # Flags ---------------------- 
    rm.add_flag(reused_flags["-y"])
    
    return rm
    
# --------------------------------------------------------------------
# --------------------------------------------------------------------
rm_logger = logging.getLogger(__name__)
def rm(args:list=[], options:dict={}, flags:list=[], nested_cmd:dict={}):
    cl = client.get_client()
    if cl is None: 
        msg = (" No existe el contenedor cliente en la plataforma")
        rm_logger.error(msg)
        return
    delete(args=[cl.name], options=options, flags=flags)
    