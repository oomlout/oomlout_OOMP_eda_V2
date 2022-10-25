
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "BatteryHolder_LINX_BAT-HLD-012-SMT"
    hexID = "FZKBATBATHOLDERLINXBATHLD12S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BatteryHolder_LINX_BAT-HLD-012-SMT', 'description': 'SMT battery holder for CR1216/1220/1225, https://linxtechnologies.com/wp/wp-content/uploads/bat-hld-012-smt.pdf', 'tags': 'battery holder coin cell cr1216 cr1220 cr1225', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_LINX_BAT-HLD-012-SMT.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Battery : BatteryHolder_LINX_BAT-HLD-012-SMT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

