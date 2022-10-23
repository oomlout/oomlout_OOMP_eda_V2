
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Heatsink"
    oIndex = "Heatsink_Fischer_SK129-STS_42x25mm_2xDrill2.5mm"
    hexID = "FZKHHFISCHERSK129STS42X252XDRILL25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Heatsink_Fischer_SK129-STS_42x25mm_2xDrill2.5mm', 'description': 'Heatsink, Fischer SK129', 'tags': 'heatsink fischer', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Heatsink.3dshapes/Heatsink_Fischer_SK129-STS_42x25mm_2xDrill2.5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Heatsink : Heatsink_Fischer_SK129-STS_42x25mm_2xDrill2.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

