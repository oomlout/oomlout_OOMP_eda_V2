
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TestPoint"
    oIndex = "TestPoint_THTPad_D2.5mm_Drill1.2mm"
    hexID = "FZKTPTPTHTPADD25DRILL12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TestPoint_THTPad_D2.5mm_Drill1.2mm', 'description': 'THT pad as test Point, diameter 2.5mm, hole diameter 1.2mm ', 'tags': 'test point THT pad', 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('TestPoint : TestPoint_THTPad_D2.5mm_Drill1.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

