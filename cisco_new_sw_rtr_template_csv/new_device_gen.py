import csv
import os
from jinja2 import Template



source_file = "sw_rtr_baselines.csv"    
template_file = "new_device_template.j2" 

#open the template_file and assign to variable f
with open (template_file) as f: 
    #reading jinja2 environment and assigning to var interface template
    interface_template = Template(f.read(), keep_trailing_newline=True) 
    

with open(source_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        device_data = interface_template.render(
            
            device_type = row['DEVICE_TYPE'],
            hostname = row['HOSTNAME'],
            domain = row['DOMAIN'],
            username = row['USERNAME'],
            password = row['PASSWORD'],
            secret_pass = row['SECRET_PASS'],
            mgmt_vlan = row['MGMT_VLAN'],
            mgmt_ip = row['MGMT_IP'],
            wan_interface = row['WAN_INTERFACE'],
            vty_conn = row['VTY_CONN'],
            radius_srv= row['RADIUS_SRV'],
            ntp_srv = row['NTP_SRV'],
            mgmt_mask= row['MGMT_MASK'],
            )
        
        
        with open(os.path.join('config_dir', row['HOSTNAME'] + '.txt'), "w") as f:
            f.write(device_data)


