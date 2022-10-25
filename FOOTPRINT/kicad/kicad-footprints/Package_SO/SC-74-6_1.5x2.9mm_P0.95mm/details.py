
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SC-74-6_1.5x2.9mm_P0.95mm"
    hexID = "FZKSOSC74615X29P95"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SC-74-6_1.5x2.9mm_P0.95mm', 'description': 'SC-74, 6 Pin (https://www.nxp.com/docs/en/package-information/SOT457.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SC-74 SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SC-74-6_1.5x2.9mm_P0.95mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SC-74-6_1.5x2.9mm_P0.95mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

