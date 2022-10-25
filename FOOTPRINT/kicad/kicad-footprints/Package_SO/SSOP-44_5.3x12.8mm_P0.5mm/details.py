
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SSOP-44_5.3x12.8mm_P0.5mm"
    hexID = "FZKSOSS4453X128P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SSOP-44_5.3x12.8mm_P0.5mm', 'description': '44-Lead Plastic Shrink Small Outline (SS)-5.30 mm Body [SSOP] (http://cds.linear.com/docs/en/datasheet/680313fa.pdf)', 'tags': 'SSOP 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSOP-44_5.3x12.8mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : SSOP-44_5.3x12.8mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

