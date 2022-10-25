
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "BGA-400_21.0x21.0mm_Layout20x20_P1.0mm"
    hexID = "FZKBGABGA421X21LAYOUT2X2P1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BGA-400_21.0x21.0mm_Layout20x20_P1.0mm', 'description': 'BGA-400, https://www.xilinx.com/support/documentation/package_specs/fg400.pdf', 'tags': 'BGA-400', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-400_21.0x21.0mm_Layout20x20_P1.0mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : BGA-400_21.0x21.0mm_Layout20x20_P1.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

