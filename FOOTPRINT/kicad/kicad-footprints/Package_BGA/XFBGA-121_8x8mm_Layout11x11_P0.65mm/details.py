
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "XFBGA-121_8x8mm_Layout11x11_P0.65mm"
    hexID = "FZKBGAXFBGA1218X8LAYOUT11X11P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'XFBGA-121_8x8mm_Layout11x11_P0.65mm', 'description': 'XFBGA-121, https://www.nxp.com/docs/en/package-information/SOT1533-1.pdf', 'tags': 'XFBGA-121', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/XFBGA-121_8x8mm_Layout11x11_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : XFBGA-121_8x8mm_Layout11x11_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

