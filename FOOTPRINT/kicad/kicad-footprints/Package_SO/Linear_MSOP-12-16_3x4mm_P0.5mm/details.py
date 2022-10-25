
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "Linear_MSOP-12-16_3x4mm_P0.5mm"
    hexID = "FZKSOLINEARMS12163X4P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Linear_MSOP-12-16_3x4mm_P0.5mm', 'description': '12-Lead Plastic Micro Small Outline Package (MS) [MSOP], variant of MSOP-16 (see https://www.analog.com/media/en/technical-documentation/data-sheets/3748fb.pdf)', 'tags': 'SSOP 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/Linear_MSOP-12-16_3x4mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : Linear_MSOP-12-16_3x4mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

