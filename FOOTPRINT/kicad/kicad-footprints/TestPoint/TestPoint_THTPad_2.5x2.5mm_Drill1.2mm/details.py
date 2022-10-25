
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TestPoint"
    oIndex = "TestPoint_THTPad_2.5x2.5mm_Drill1.2mm"
    hexID = "FZKTPTPTHTPAD25X25DRILL12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TestPoint_THTPad_2.5x2.5mm_Drill1.2mm', 'description': 'THT rectangular pad as test Point, square 2.5mm side length, hole diameter 1.2mm', 'tags': 'test point THT pad rectangle square', 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TestPoint : TestPoint_THTPad_2.5x2.5mm_Drill1.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

