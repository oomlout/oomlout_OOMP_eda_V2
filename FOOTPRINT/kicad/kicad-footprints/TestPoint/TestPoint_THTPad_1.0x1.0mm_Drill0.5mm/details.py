
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TestPoint"
    oIndex = "TestPoint_THTPad_1.0x1.0mm_Drill0.5mm"
    hexID = "FZKTPTPTHTPAD1X1DRILL5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TestPoint_THTPad_1.0x1.0mm_Drill0.5mm', 'description': 'THT rectangular pad as test Point, square 1.0mm side length, hole diameter 0.5mm', 'tags': 'test point THT pad rectangle square', 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TestPoint : TestPoint_THTPad_1.0x1.0mm_Drill0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

