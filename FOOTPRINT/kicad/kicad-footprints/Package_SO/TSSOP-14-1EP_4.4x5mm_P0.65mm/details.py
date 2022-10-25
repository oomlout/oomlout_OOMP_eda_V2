
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "TSSOP-14-1EP_4.4x5mm_P0.65mm"
    hexID = "FZKSOTSS141EP44X5P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TSSOP-14-1EP_4.4x5mm_P0.65mm', 'description': '14-Lead Plastic Thin Shrink Small Outline (ST)-4.4 mm Body [TSSOP] with exposed pad (http://cds.linear.com/docs/en/datasheet/34301fa.pdf)', 'tags': 'SSOP 0.65 exposed pad', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TSSOP-14-1EP_4.4x5mm_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : TSSOP-14-1EP_4.4x5mm_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

