
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "BGA-96_9.0x13.0mm_Layout2x3x16_P0.8mm"
    hexID = "FZKBGABGA969X13LAYOUT2X3X16P8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BGA-96_9.0x13.0mm_Layout2x3x16_P0.8mm', 'description': 'BGA-96, http://www.mouser.com/ds/2/198/43-46TR16640B-81280BL-706483.pdf', 'tags': 'BGA-96', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-96_9.0x13.0mm_Layout2x3x16_P0.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : BGA-96_9.0x13.0mm_Layout2x3x16_P0.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

