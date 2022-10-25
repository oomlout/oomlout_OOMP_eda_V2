
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TestPoint"
    oIndex = "TestPoint_Pad_D2.0mm"
    hexID = "FZKTPTPPADD2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TestPoint_Pad_D2.0mm', 'description': 'SMD pad as test Point, diameter 2.0mm', 'tags': 'test point SMD pad', 'attributeType': None, 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('TestPoint : TestPoint_Pad_D2.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

