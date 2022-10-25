
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "HSOP-32-1EP_7.5x11mm_P0.65mm_EP4.7x4.7mm"
    hexID = "FZKSOHS321EP75X11P65EP47X47"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HSOP-32-1EP_7.5x11mm_P0.65mm_EP4.7x4.7mm', 'description': 'HSOP, 32 Pin (https://www.nxp.com/docs/en/package-information/SOT1746-3.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'HSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HSOP-32-1EP_7.5x11mm_P0.65mm_EP4.7x4.7mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : HSOP-32-1EP_7.5x11mm_P0.65mm_EP4.7x4.7mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

