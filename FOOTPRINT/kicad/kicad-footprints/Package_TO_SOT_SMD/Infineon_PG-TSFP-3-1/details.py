
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_SMD"
    oIndex = "Infineon_PG-TSFP-3-1"
    hexID = "FZKPACKAGETOSOTSMINFINEONPGTSFP31"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_PG-TSFP-3-1', 'description': 'Infineon_PG-TSFP-3-1, https://www.infineon.com/dgdl/TSFP-3-1,-2-Package_Overview.pdf?fileId=db3a30431936bc4b0119539929863d46', 'tags': 'TSFP-3', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/Infineon_PG-TSFP-3-1.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_SMD : Infineon_PG-TSFP-3-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

