
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "TSOP-I-28_11.8x8mm_P0.55mm"
    hexID = "FZKSOTSI28118X8P55"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TSOP-I-28_11.8x8mm_P0.55mm', 'description': 'TSOP I, 28 pins, 18.8x8mm body, 0.55mm pitch, IPC-calculated pads (http://ww1.microchip.com/downloads/en/devicedoc/doc0807.pdf)', 'tags': 'TSOP I 28 pins', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TSOP-I-28_11.8x8mm_P0.55mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : TSOP-I-28_11.8x8mm_P0.55mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

