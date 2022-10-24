
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "BGA-144_13.0x13.0mm_Layout12x12_P1.0mm"
    hexID = "FZKBGABGA14413X13LAYOUT12X12P1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BGA-144_13.0x13.0mm_Layout12x12_P1.0mm', 'description': 'BGA-144, http://www.topline.tv/drawings/pdf/BGA%201,0mm%20pitch/LBGA144T1.0-DC128.pdf', 'tags': 'BGA-144', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-144_13.0x13.0mm_Layout12x12_P1.0mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : BGA-144_13.0x13.0mm_Layout12x12_P1.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

