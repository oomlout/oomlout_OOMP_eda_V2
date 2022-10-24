
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "UFBGA-32_4.0x4.0mm_Layout6x6_P0.5mm"
    hexID = "FZKBGAUFBGA324X4LAYOUT6X6P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UFBGA-32_4.0x4.0mm_Layout6x6_P0.5mm', 'description': 'UFBGA-32, 6x6, 4x4mm package, pitch 0.5mm', 'tags': 'UFBGA-32', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/UFBGA-32_4.0x4.0mm_Layout6x6_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : UFBGA-32_4.0x4.0mm_Layout6x6_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

