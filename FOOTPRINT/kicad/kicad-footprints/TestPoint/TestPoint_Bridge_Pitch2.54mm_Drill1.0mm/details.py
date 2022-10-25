
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TestPoint"
    oIndex = "TestPoint_Bridge_Pitch2.54mm_Drill1.0mm"
    hexID = "FZKTPTPBRIDGEPITCH254DRILL1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TestPoint_Bridge_Pitch2.54mm_Drill1.0mm', 'description': 'wire loop as test point, pitch 2.54mm, hole diameter 1.0mm, wire diameter 0.8mm', 'tags': 'test point wire loop', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TestPoint.3dshapes/TestPoint_Bridge_Pitch2.54mm_Drill1.0mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('TestPoint : TestPoint_Bridge_Pitch2.54mm_Drill1.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

