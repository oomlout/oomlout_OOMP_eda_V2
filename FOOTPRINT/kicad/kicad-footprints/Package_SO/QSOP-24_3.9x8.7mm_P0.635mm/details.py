
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "QSOP-24_3.9x8.7mm_P0.635mm"
    hexID = "FZKSOQS2439X87P635"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QSOP-24_3.9x8.7mm_P0.635mm', 'description': '24-Lead Plastic Shrink Small Outline Narrow Body (QR)-.150" Body [QSOP] (see Microchip Packaging Specification 00000049CH.pdf)', 'tags': 'QSOP 0.635', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/QSOP-24_3.9x8.7mm_P0.635mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : QSOP-24_3.9x8.7mm_P0.635mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

