
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "BGA-625_21.0x21.0mm_Layout25x25_P0.8mm"
    hexID = "FZKBGABGA62521X21LAYOUT25X25P8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BGA-625_21.0x21.0mm_Layout25x25_P0.8mm', 'description': 'BGA-625', 'tags': 'BGA-625', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-625_21.0x21.0mm_Layout25x25_P0.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : BGA-625_21.0x21.0mm_Layout25x25_P0.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

