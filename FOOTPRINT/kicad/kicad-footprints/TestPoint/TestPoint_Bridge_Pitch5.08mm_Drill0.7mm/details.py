
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TestPoint"
    oIndex = "TestPoint_Bridge_Pitch5.08mm_Drill0.7mm"
    hexID = "FZKTPTPBRIDGEPITCH58DRILL7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TestPoint_Bridge_Pitch5.08mm_Drill0.7mm', 'description': 'wire loop as test point, pitch 5.08mm, hole diameter 0.7mm, wire diameter 1.0mm', 'tags': 'test point wire loop', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TestPoint.3dshapes/TestPoint_Bridge_Pitch5.08mm_Drill0.7mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('TestPoint : TestPoint_Bridge_Pitch5.08mm_Drill0.7mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

