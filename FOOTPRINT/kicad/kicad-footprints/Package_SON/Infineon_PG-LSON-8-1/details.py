
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "Infineon_PG-LSON-8-1"
    hexID = "FZKSONINFINEONPGLSON81"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_PG-LSON-8-1', 'description': 'https://www.infineon.com/cms/en/product/packages/PG-LSON/PG-LSON-8-1/', 'tags': 'PG-LSON-8-1', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Infineon_PG-LSON-8-1.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : Infineon_PG-LSON-8-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

