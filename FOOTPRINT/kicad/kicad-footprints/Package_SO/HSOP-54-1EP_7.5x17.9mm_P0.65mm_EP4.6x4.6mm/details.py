
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "HSOP-54-1EP_7.5x17.9mm_P0.65mm_EP4.6x4.6mm"
    hexID = "FZKSOHS541EP75X179P65EP46X46"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HSOP-54-1EP_7.5x17.9mm_P0.65mm_EP4.6x4.6mm', 'description': 'HSOP, 54 Pin (https://www.nxp.com/docs/en/package-information/98ASA10506D.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'HSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HSOP-54-1EP_7.5x17.9mm_P0.65mm_EP4.6x4.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : HSOP-54-1EP_7.5x17.9mm_P0.65mm_EP4.6x4.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

