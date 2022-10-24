
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "VFBGA-49_5.0x5.0mm_Layout7x7_P0.65mm"
    hexID = "FZKBGAVFBGA495X5LAYOUT7X7P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VFBGA-49_5.0x5.0mm_Layout7x7_P0.65mm', 'description': 'VFBGA-49, 7x7, 5x5mm package, pitch 0.65mm', 'tags': 'VFBGA-49', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/VFBGA-49_5.0x5.0mm_Layout7x7_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : VFBGA-49_5.0x5.0mm_Layout7x7_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

