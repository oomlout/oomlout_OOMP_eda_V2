
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "BatteryHolder_Keystone_3034_1x20mm"
    hexID = "FZKBATBATHOLDERKEYSTONE3341X2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BatteryHolder_Keystone_3034_1x20mm', 'description': 'Keystone 3034 SMD battery holder for 2020, 2025 and 2032 coincell batteries. http://www.keyelco.com/product-pdf.cfm?p=798', 'tags': 'Keystone type 3034 coin cell retainer', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_Keystone_3034_1x20mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Battery : BatteryHolder_Keystone_3034_1x20mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

