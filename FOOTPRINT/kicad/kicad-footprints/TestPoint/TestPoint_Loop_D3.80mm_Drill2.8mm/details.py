
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TestPoint"
    oIndex = "TestPoint_Loop_D3.80mm_Drill2.8mm"
    hexID = "FZKTPTPLOOPD38DRILL28"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TestPoint_Loop_D3.80mm_Drill2.8mm', 'description': 'wire loop as test point, loop diameter 3.8mm, hole diameter 2.8mm', 'tags': 'test point wire loop bead', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TestPoint.3dshapes/TestPoint_Loop_D3.80mm_Drill2.8mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('TestPoint : TestPoint_Loop_D3.80mm_Drill2.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

