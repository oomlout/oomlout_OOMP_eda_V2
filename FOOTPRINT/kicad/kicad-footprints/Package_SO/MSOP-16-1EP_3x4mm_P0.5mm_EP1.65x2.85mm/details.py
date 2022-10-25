
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "MSOP-16-1EP_3x4mm_P0.5mm_EP1.65x2.85mm"
    hexID = "FZKSOMS161EP3X4P5EP165X285"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MSOP-16-1EP_3x4mm_P0.5mm_EP1.65x2.85mm', 'description': 'MSOP, 16 Pin (http://cds.linear.com/docs/en/datasheet/37551fd.pdf#page=23), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'MSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/MSOP-16-1EP_3x4mm_P0.5mm_EP1.65x2.85mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : MSOP-16-1EP_3x4mm_P0.5mm_EP1.65x2.85mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

