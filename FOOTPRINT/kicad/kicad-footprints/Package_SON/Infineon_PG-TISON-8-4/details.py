
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "Infineon_PG-TISON-8-4"
    hexID = "FZKSONINFINEONPGTISON84"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_PG-TISON-8-4', 'description': 'Infineon, PG-TISON-8-4, 5x6x1.15mm, 1.27mm Pitch, Exposed Paddle, https://www.infineon.com/cms/en/product/packages/PG-TISON/PG-TISON-8-4/', 'tags': 'tison', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Infineon_PG-TISON-8-4.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : Infineon_PG-TISON-8-4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

