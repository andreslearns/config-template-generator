import csv
from jinja2 import Template


#store the source csv in variable
source_file = "interface_source.csv"    
# store the jinja2 file in a variable
template_file = "interface_template.j2" 

#create an empty string for the ouput container
output_configs =""   

#open the template_file and assign to variable f
with open (template_file) as f: 
    #reading jinja2 environment and assigning to var interface template
    interface_template = Template(f.read(), keep_trailing_newline=True) 
    
# opening the csv file and assigning to var f
with open(source_file) as f:
    reader = csv.DictReader(f) #reading the csv file
    for row in reader:  #loop in all rows of csv file and assigning to row variable
        interface_data = interface_template.render(   #assigned all the rendered file into variables
            # assigning all the row values into variables                                       
            interface = row['Interface'],
            vlan = row['VLAN'],
            server = row['Server'],
            link = row['Link'],
            purpose = row['Purpose'],)
        output_configs += interface_data #appending all the values from interface_data to output_configs

with open("interface_config.txt", 'w') as f:
    f.write(output_configs)