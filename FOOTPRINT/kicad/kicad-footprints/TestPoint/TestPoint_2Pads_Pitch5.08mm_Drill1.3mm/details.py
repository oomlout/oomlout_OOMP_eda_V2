
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TestPoint"
    oIndex = "TestPoint_2Pads_Pitch5.08mm_Drill1.3mm"
    hexID = "FZKTPTP2PADSPITCH58DRILL13"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TestPoint_2Pads_Pitch5.08mm_Drill1.3mm', 'description': 'Test point with 2 pads, pitch 5.08mm, hole diameter 1.3mm, wire diameter 1.0mm', 'tags': 'CONN DEV', 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('TestPoint : TestPoint_2Pads_Pitch5.08mm_Drill1.3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

