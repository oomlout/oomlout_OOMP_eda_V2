
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "BGA-1023_33.0x33.0mm_Layout32x32_P1.0mm"
    hexID = "FZKBGABGA12333X33LAYOUT32X32P1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BGA-1023_33.0x33.0mm_Layout32x32_P1.0mm', 'description': 'BGA-1023', 'tags': 'BGA-1023', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-1023_33.0x33.0mm_Layout32x32_P1.0mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : BGA-1023_33.0x33.0mm_Layout32x32_P1.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

