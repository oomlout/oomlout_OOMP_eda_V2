
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TestPoint"
    oIndex = "TestPoint_Pad_3.0x3.0mm"
    hexID = "FZKTPTPPAD3X3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TestPoint_Pad_3.0x3.0mm', 'description': 'SMD rectangular pad as test Point, square 3.0mm side length', 'tags': 'test point SMD pad rectangle square', 'attributeType': None, 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('TestPoint : TestPoint_Pad_3.0x3.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

