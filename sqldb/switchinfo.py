#!/usr/bin/python3

import sqlite3
from napalm import get_network_driver


def first_run():
    conn = sqlite3.connect("swinfo.db")
    try:
        conn.execute("CREATE TABLE IF NOT EXISTS switches (hostname CHAR, IP CHAR, startup_config CHAR, running_config CHAR, valide_config BOOL)")

        conn.execute("INSERT INTO SWITCHES (HOSTNAME,IP) VALUES ('SW-1', '10.9.124.209')")
        conn.execute("INSERT INTO SWITCHES (HOSTNAME,IP) VALUES ('SW-2', '10.3.174.181')")
        conn.commit()
    except sqlite3.OperationalError as err:
        print(err)
    finally:
        conn.close()

def retrv_conf():
    device = get_network_driver('eos')
    device = driver('sw-1','admin','alta3')
    device.open()
    sw_conf = device.get_config()
    return sw_conf

def update_sw_conf():
    conn = sqlite3.connect("swinfo.db")
    sw_conf = retrv_conf(sw)
    run_conf = sw_conf['running']
    start_conf = sw_conf['startup']
    conn.execute(f"Update switches SET running_config - '{run_conf}' where hostname= '{sw}'")
    conn.execute(f"Update switches SET startup_config - '{start_conf}' where hostname= '{sw}'")
    conn.commit()
      
def comply(sw):
    driver = get_network_driver('eos')
    device = driver(sw, 'admin', 'alta3')
    device.open()
    complies = device.compliance_report("/home/student/pyna/{sw}_validate.yml")
    device.close()
    if complies['complies']:
        compliant = True 
    else:
        compliant = False
    return compliant

print(comply())       

