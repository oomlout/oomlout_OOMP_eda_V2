
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TestPoint"
    oIndex = "TestPoint_THTPad_1.5x1.5mm_Drill0.7mm"
    hexID = "FZKTPTPTHTPAD15X15DRILL7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TestPoint_THTPad_1.5x1.5mm_Drill0.7mm', 'description': 'THT rectangular pad as test Point, square 1.5mm side length, hole diameter 0.7mm', 'tags': 'test point THT pad rectangle square', 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TestPoint : TestPoint_THTPad_1.5x1.5mm_Drill0.7mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

