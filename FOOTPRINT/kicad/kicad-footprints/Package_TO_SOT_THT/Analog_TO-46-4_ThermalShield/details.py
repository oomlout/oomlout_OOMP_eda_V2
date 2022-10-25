
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "Analog_TO-46-4_ThermalShield"
    hexID = "FZKSOTANALOGTO464THERMALSH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Analog_TO-46-4_ThermalShield', 'description': 'TO-46-4 with Valox case, based on https://www.analog.com/media/en/technical-documentation/data-sheets/199399fc.pdf', 'tags': 'TO-46-4 LM399', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/Analog_TO-46-4_ThermalShield.wrl', 'pins': {'type': 'thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Package_TO_SOT_THT : Analog_TO-46-4_ThermalShield')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

