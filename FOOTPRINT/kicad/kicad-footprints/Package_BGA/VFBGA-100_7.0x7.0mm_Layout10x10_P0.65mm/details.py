
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "VFBGA-100_7.0x7.0mm_Layout10x10_P0.65mm"
    hexID = "FZKBGAVFBGA17X7LAYOUT1X1P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VFBGA-100_7.0x7.0mm_Layout10x10_P0.65mm', 'description': 'VFBGA-100, 10x10, 7x7mm package, pitch 0.65mm', 'tags': 'VFBGA-100', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/VFBGA-100_7.0x7.0mm_Layout10x10_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : VFBGA-100_7.0x7.0mm_Layout10x10_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

