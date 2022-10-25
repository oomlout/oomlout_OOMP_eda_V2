
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "HVSSOP-10-1EP_3x3mm_P0.5mm_EP1.57x1.88mm"
    hexID = "FZKSOHVSS11EP3X3P5EP157X188"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HVSSOP-10-1EP_3x3mm_P0.5mm_EP1.57x1.88mm', 'description': 'HVSSOP, 10 Pin (https://www.ti.com/lit/ds/symlink/bq24090.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'HVSSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HVSSOP-10-1EP_3x3mm_P0.5mm_EP1.57x1.88mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : HVSSOP-10-1EP_3x3mm_P0.5mm_EP1.57x1.88mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

