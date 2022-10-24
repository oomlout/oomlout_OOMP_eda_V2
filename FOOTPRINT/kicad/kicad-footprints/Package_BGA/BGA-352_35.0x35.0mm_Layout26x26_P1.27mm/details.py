
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "BGA-352_35.0x35.0mm_Layout26x26_P1.27mm"
    hexID = "FZKBGABGA35235X35LAYOUT26X26P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BGA-352_35.0x35.0mm_Layout26x26_P1.27mm', 'description': 'BGA-352, https://www.fujitsu.com/downloads/MICRO/fma/pdfmcu/b352p05.pdf', 'tags': 'BGA-352', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-352_35.0x35.0mm_Layout26x26_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : BGA-352_35.0x35.0mm_Layout26x26_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

