
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "MSOP-10-1EP_3x3mm_P0.5mm_EP1.68x1.88mm"
    hexID = "FZKSOMS11EP3X3P5EP168X188"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MSOP-10-1EP_3x3mm_P0.5mm_EP1.68x1.88mm', 'description': 'MSOP, 10 Pin (https://www.analog.com/media/en/technical-documentation/data-sheets/3805fg.pdf#page=18), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'MSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/MSOP-10-1EP_3x3mm_P0.5mm_EP1.68x1.88mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : MSOP-10-1EP_3x3mm_P0.5mm_EP1.68x1.88mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

