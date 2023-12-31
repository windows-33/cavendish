from fastapi import FastAPI, APIRouter, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from models.users import User
from models.hdd import HDD
from models.cpu import CPU
from models.mainboard import Mainboard, MainboardPCI
from models.ram import RAM
from models.gpu import GPU
from models.case import Case
from models.cooler import Cooler
from models.ssd import SSD
from models.quotation import Quotation
from models.programs import Program
from models.power import Power
import re

from .com_data import ram_com
from .common import decimal_to_name

from schemas.search import ProcessListStep1

from db.connection import engineconn

engine = engineconn()
session = engine.sessionmaker()

def gpu_com_cpu(gpu, cpu):
    gpu_interface = gpu.interface
    cpu_pcie_version = cpu.pcie_version
    if gpu_interface == None or gpu_interface == "" or cpu_pcie_version == None or cpu_pcie_version == 0:
        return False
    else:
        if len(gpu_interface) < 5:
            return False
        gpu_i = re.search(r'(\d+\.\d+)', gpu_interface)
        if gpu_i == None or gpu_i == "":
            return False
        gpu_i = int(gpu_i.group(0)[0])
        if cpu_pcie_version % 2 == 1:
            if gpu_i >= 3:
                return True
        elif (cpu_pcie_version / 2) % 2 == 1:
            if 3 <= gpu_i <= 4:
                return True
        elif (cpu_pcie_version / 4) % 2 == 1:
            if gpu_i == 3:
                return True    
        return False 

def gpu_com_mainboard(gpu, mainboard):
    gpu_interface = gpu.interface
    mainboard_vga_connection = mainboard.vga_connection
    if mainboard_vga_connection == None or mainboard_vga_connection == "" or gpu_interface == None or gpu_interface == "":
        return False
    else:
        if len(gpu_interface) < 5 or len(mainboard_vga_connection) < 5:
            return False
        gpu_i = re.search(r'(\d+\.\d+)', gpu_interface)
        mb_vc = re.search(r'(\d+\.\d+)', mainboard_vga_connection)
        if gpu_i == None or gpu_i == "":
            if mb_vc == None or mb_vc == "":
                return True
            return False
        
        gpu_i = int(gpu_i.group(0)[0])
        mb_vc = int(mb_vc.group(0)[0])

        if mb_vc >= gpu_i:
            return True
        return False    

def gpu_com_case(gpu, case):
    gpu_length = gpu.length
    case_gpu_size = case.gpu_size
    if gpu_length == None or gpu_length == 0 or case_gpu_size == None or case_gpu_size == 0:
        return False
    if gpu_length <= case_gpu_size:
        return True
    else:
        return False

def gpu_com_power(gpu, power):
    gpu_recommend_power = gpu.recommend_power
    power_rated_power = power.rated_power
    if gpu_recommend_power == None or gpu_recommend_power == 0 or power_rated_power == None or power_rated_power == 0:
        return False
    if gpu_recommend_power <= power_rated_power:
        return True
    gpu_pin = gpu.pin
    pcie_16pin = power.pcie_16pin
    pcie_8pin = power.pcie_8pin
    pcie_6pin = power.pcie_6pin

    if gpu_pin == None or gpu_pin == 0:
        return False
    if pcie_16pin == None or pcie_16pin == 0:
        pass
    else:
        if len(gpu_pin) == 3:
            if gpu_pin[-3] != "0":
                return True
        elif len(gpu_pin) > 3:
            if gpu_pin[-3] != "0" or gpu_pin[-4] != "0":
                return True
    if pcie_8pin == None or pcie_8pin == 0:
        pass
    else:
        if len(gpu_pin) >= 5:
            if gpu_pin[-3] != "0":
                return True
    if pcie_6pin == None or pcie_6pin == 0:
        pass
    else:
        if len(gpu_pin) >= 6:
            if gpu_pin[-3] != "0":
                return True

    return False
