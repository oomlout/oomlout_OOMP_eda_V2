
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "Infineon_PG-TSDSO-14-22"
    hexID = "FZKSOINFINEONPGTSDSO1422"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_PG-TSDSO-14-22', 'description': 'Infineon_PG-TSDSO-14-22', 'tags': 'Infineon TSDSO 14-22 ', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/Infineon_PG-TSDSO-14-22.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : Infineon_PG-TSDSO-14-22')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

