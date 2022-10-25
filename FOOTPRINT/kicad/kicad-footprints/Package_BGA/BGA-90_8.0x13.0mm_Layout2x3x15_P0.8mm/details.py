
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "BGA-90_8.0x13.0mm_Layout2x3x15_P0.8mm"
    hexID = "FZKBGABGA98X13LAYOUT2X3X15P8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BGA-90_8.0x13.0mm_Layout2x3x15_P0.8mm', 'description': 'BGA-90, http://www.issi.com/WW/pdf/42-45S32800J.pdf', 'tags': 'BGA-90', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-90_8.0x13.0mm_Layout2x3x15_P0.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : BGA-90_8.0x13.0mm_Layout2x3x15_P0.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

