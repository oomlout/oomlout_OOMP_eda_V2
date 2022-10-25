
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "MSOP-12-1EP_3x4mm_P0.65mm_EP1.65x2.85mm"
    hexID = "FZKSOMS121EP3X4P65EP165X285"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MSOP-12-1EP_3x4mm_P0.65mm_EP1.65x2.85mm', 'description': 'MSOP, 12 Pin (https://www.analog.com/media/en/technical-documentation/data-sheets/3652fe.pdf#page=24), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'MSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/MSOP-12-1EP_3x4mm_P0.65mm_EP1.65x2.85mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : MSOP-12-1EP_3x4mm_P0.65mm_EP1.65x2.85mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

