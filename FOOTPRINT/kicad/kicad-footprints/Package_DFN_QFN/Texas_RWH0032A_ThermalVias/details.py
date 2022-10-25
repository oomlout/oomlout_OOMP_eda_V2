
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Texas_RWH0032A_ThermalVias"
    hexID = "FZKDFNTEXASRWH32ATHERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_RWH0032A_ThermalVias', 'description': 'Texas Instruments, RWH0032A, 8x8x0.9mm (http://www.ti.com/lit/ds/snosd10c/snosd10c.pdf)', 'tags': 'ti rwh0032a', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_RWH0032A.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : Texas_RWH0032A_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

