
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TestPoint"
    oIndex = "TestPoint_2Pads_Pitch2.54mm_Drill0.8mm"
    hexID = "FZKTPTP2PADSPITCH254DRILL8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TestPoint_2Pads_Pitch2.54mm_Drill0.8mm', 'description': 'Test point with 2 pins, pitch 2.54mm, drill diameter 0.8mm', 'tags': 'CONN DEV', 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('TestPoint : TestPoint_2Pads_Pitch2.54mm_Drill0.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

