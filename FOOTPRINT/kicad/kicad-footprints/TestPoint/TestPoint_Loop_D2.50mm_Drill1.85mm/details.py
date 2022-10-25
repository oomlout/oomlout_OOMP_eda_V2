
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TestPoint"
    oIndex = "TestPoint_Loop_D2.50mm_Drill1.85mm"
    hexID = "FZKTPTPLOOPD25DRILL185"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TestPoint_Loop_D2.50mm_Drill1.85mm', 'description': 'wire loop as test point, loop diameter 2.5mm, hole diameter 1.85mm', 'tags': 'test point wire loop bead', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TestPoint.3dshapes/TestPoint_Loop_D2.50mm_Drill1.85mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('TestPoint : TestPoint_Loop_D2.50mm_Drill1.85mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

