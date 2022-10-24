
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TestPoint"
    oIndex = "TestPoint_THTPad_D1.0mm_Drill0.5mm"
    hexID = "FZKTPTPTHTPADD1DRILL5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TestPoint_THTPad_D1.0mm_Drill0.5mm', 'description': 'THT pad as test Point, diameter 1.0mm, hole diameter 0.5mm', 'tags': 'test point THT pad', 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('TestPoint : TestPoint_THTPad_D1.0mm_Drill0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

