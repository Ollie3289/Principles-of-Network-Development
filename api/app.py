from flask import Flask, jsonify, request
import json
import yaml
import xml.etree.ElementTree as ET


app = Flask(__name__)



#===========================================
# Read router config from Practical 3
#===========================================

#===========================================
#Home Topologies
#===========================================

with open("../configuration/home_topology/router1.json") as file:
    home_router1 = json.load(file)

with open("../configuration/home_topology/router2.json") as file:
    home_router2 = json.load(file)

with open("../configuration/home_topology/switch1.yaml") as file:
    home_switch1 = yaml.safe_load(file)

with open("../configuration/home_topology/switch2.yaml") as file:
    home_switch2 = yaml.safe_load(file)

with open("../configuration/home_topology/laptop1.json") as file:
    home_laptop1 = json.load(file)

with open("../configuration/home_topology/laptop2.json") as file:
    home_laptop2 = json.load(file)

with open("../configuration/home_topology/mobile1.json") as file:
    home_mobile1 = json.load(file)

with open("../configuration/home_topology/mobile2.json") as file:
    home_mobile2 = json.load(file)

with open("../configuration/home_topology/printer1.json") as file:
    home_printer1 = json.load(file)

#=================================
# Office Topologies
#=================================

with open("../configuration/office_topology/router1.json") as file:
    office_router1 = json.load(file)

with open("../configuration/office_topology/router2.json") as file:
    office_router2 = json.load(file)

with open("../configuration/office_topology/router3.json") as file:
    office_router3 = json.load(file)

with open("../configuration/office_topology/router4.json") as file:
    office_router4 = json.load(file)

with open("../configuration/office_topology/laptop1.json") as file:
    office_laptop1 = json.load(file)

with open("../configuration/office_topology/laptop2.json") as file:
    office_laptop2 = json.load(file)

with open("../configuration/office_topology/pc1.json") as file:
    office_pc1 = json.load(file)

with open("../configuration/office_topology/pc2.json") as file:
    office_pc2 = json.load(file)

with open("../configuration/office_topology/phone1.json") as file:
    office_phone1 = json.load(file)

with open("../configuration/office_topology/phone2.json") as file:
    office_phone2 = json.load(file)

with open("../configuration/office_topology/switch1.yaml") as file:
    office_switch1 = yaml.safe_load(file)

with open("../configuration/office_topology/switch2.yaml") as file:
    office_switch2 = yaml.safe_load(file)

with open("../configuration/office_topology/printer1.json") as file:
    office_printer1 = json.load(file)



#===================================
# Cloud Servers
#===================================

with open("../configuration/cloud/api_server.json") as file:
    api_server = json.load(file)

with open("../configuration/cloud/authentication_server.json") as file:
    authentication_server = json.load(file)

with open("../configuration/cloud/database_server.json") as file:
    database_server = json.load(file)


routers = [
    home_router1, 
    home_router2
   ]

laptops = [
    home_laptop1, 
    home_laptop2
  ]

mobiles = [
    home_mobile1, 
    home_mobile2
  ]

printers = [
    home_printer1
]

switches = [
    home_switch1,
    home_switch2
]

servers = [
    api_server,
    authentication_server,
    database_server
]

office_routers = [
    office_router1,
    office_router2,
    office_router3,
    office_router4
]


office_switches = [
    office_switch1,
    office_switch2
]


office_laptops = [
    office_laptop1,
    office_laptop2
]


office_pcs = [
    office_pc1,
    office_pc2
]


office_phones = [
    office_phone1,
    office_phone2
]


office_printers = [
    office_printer1
]

home_devices = (
    routers +
    switches +
    laptops +
    mobiles +
    printers
)


office_devices = (
    office_routers +
    office_switches +
    office_laptops +
    office_pcs +
    office_phones +
    office_printers
)


devices = (
    routers +
    switches +
    laptops +
    mobiles +
    printers +
    office_routers +
    office_switches +
    office_laptops +
    office_pcs +
    office_phones +
    office_printers +
    servers
)

#=========================================
#Cloud Server Route Directory Methods
#=========================================

@app.route('/servers')
def get_servers():
 return jsonify(servers)


#==================================
#Home Route Directory Methods
#==================================

@app.route('/home/devices')
def get_home_devices():

    return jsonify(home_devices)

#===============================
#Home Route Directoty Methods
#===============================

@app.route('/home/routers')
def get_home_routers():
    return jsonify(routers)


@app.route('/home/laptops')
def get_home_laptops():
    return jsonify(laptops)

@app.route('/home/mobiles')
def get_home_mobiles():
    return jsonify(mobiles)

@app.route('/home/printers')
def get_home_printers():
    return jsonify(printers)

@app.route('/home/switches')
def get_home_switches():
    return jsonify(switches)

#=================================    
#Office Route Directory Methods
#================================= 

@app.route('/office/devices')
def get_office_devices():
   return jsonify(office_devices)

@app.route('/office/routers')
def get_office_routers():
    return jsonify(office_routers)

@app.route('/office/switches')
def get_office_switches():
    return jsonify(office_switches)

@app.route('/office/laptops')
def get_office_laptops():
    return jsonify(office_laptops)

@app.route('/office/pcs')
def get_office_pcs():
    return jsonify(office_pcs)

@app.route('/office/phones')
def get_office_phones():
    return jsonify(office_phones)

@app.route('/office/printers')
def get_office_printers():
    return jsonify(office_printers)

#==================================
# Retrieve Home Specific Devices
#==================================

@app.route('/home/routers/<hostname>')
def get_specific_home_router(hostname):

    for router in routers:

        if router["hostname"] == hostname:
            return jsonify(router)

    return jsonify({
        "error": "Router not found"
    }), 404

@app.route('/home/laptops/<hostname>')
def get_specific_home_laptop(hostname):

    for laptop in laptops:

        if laptop["hostname"] == hostname:
            return jsonify(laptop)

    return jsonify({
        "error":"Laptop not found"
    }),404


@app.route('/home/mobiles/<hostname>')
def get_specific_home_mobile(hostname):

    for mobile in mobiles:

        if mobile["hostname"] == hostname:
            return jsonify(mobile)

    return jsonify({
        "error":"Mobile not found"
    }),404


@app.route('/home/switches/<hostname>')
def get_specific_home_switch(hostname):

    for switch in switches:

        if switch["hostname"] == hostname:
            return jsonify(switch)

    return jsonify({
        "error":"Switch not found"
    }),404


@app.route('/home/printers/<hostname>')
def get_specific_home_printer(hostname):

    for printer in printers:

        if printer["hostname"] == hostname:
            return jsonify(printer)

    return jsonify({
        "error": "Printer not found"
    }), 404

#==================================
#Retrieve Cloud Specific Server
#==================================

@app.route('/cloud/servers/<hostname>')
def get_specific_cloud_server(hostname):

    for server in servers:

        if server["hostname"] == hostname:
            return jsonify(server)

    return jsonify({
        "error": "Server not found"
    }), 404

#=====================================
# Retrieve Office Specific Devices
#=====================================

@app.route('/office/routers/<hostname>')
def get_specific_office_router(hostname):

    for router in routers:

        if router["hostname"] == hostname:
            return jsonify(router)

    return jsonify({
        "error": "Router not found"
    }), 404


@app.route('/office/switches/<hostname>')
def get_specific_office_switches(hostname):

    for switche in switches:

        if switche["hostname"] == hostname:
            return jsonify(switche)

    return jsonify({
        "error": "switche not found"
    }), 404

@app.route('/office/laptops/<hostname>')
def get_specific_office_laptop(hostname):

    for laptop in office_laptops:

        if laptop["hostname"] == hostname:
            return jsonify(laptop)

    return jsonify({
        "error": "Laptop not found"
    }), 404

@app.route('/office/pcs/<hostname>')
def get_specific_office_pc(hostname):

    for pc in office_pcs:

        if pc["hostname"] == hostname:
            return jsonify(pc)

    return jsonify({
        "error": "PC not found"
    }), 404

@app.route('/office/phones/<hostname>')
def get_specific_office_phone(hostname):

    for phone in office_phones:

        if phone["hostname"] == hostname:
            return jsonify(phone)

    return jsonify({
        "error": "Phone not found"
    }), 404




#==========================
#GET, POST PUT and DELETE
#==========================

@app.route('/devices', methods=['GET', 'POST'])
def manage_devices():

    if request.method == 'GET':
         return jsonify(devices)


    if request.method == 'POST':

         new_device = request.json

         devices.append(new_device)

         return jsonify({
             "message": "Device added successfully",
             "device": new_device
         }), 201


#==========================
# PUT Method
#==========================

@app.route('/devices/<hostname>', methods=['PUT'])
def update_device(hostname):

     updated_device = request.json

     for device in devices:

         if device["hostname"] == hostname:

             device.update(updated_device)

             return jsonify({
                 "message": "Device updated successfully",
                 "device": device
             }), 200


     return jsonify({
         "error": "Device not found"
     }), 404



#======================
# Delete method
#======================

@app.route('/devices/<hostname>', methods=['DELETE'])
def delete_device(hostname):

     for device in devices:

         if device["hostname"] == hostname:

             devices.remove(device)

             return jsonify({
                 "message": "Device deleted successfully",
                 "device": device
             }), 200


     return jsonify({
         "error": "Device not found"
     }), 404


@app.route('/routers/<hostname>')
def get_router(hostname):

    for router in routers:
        if router["hostname"] == hostname:
            return jsonify(router)

    return jsonify({
        "error": "Router not found"
    }), 404

if __name__ == '__main__':
    app.run(debug=True)