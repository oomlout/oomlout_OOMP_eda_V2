
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TestPoint"
    oIndex = "TestPoint_Bridge_Pitch6.35mm_Drill1.3mm"
    hexID = "FZKTPTPBRIDGEPITCH635DRILL13"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TestPoint_Bridge_Pitch6.35mm_Drill1.3mm', 'description': 'wire loop as test point, pitch 6.35mm, hole diameter 1.3mm, wire diameter 1.0mm', 'tags': 'test point wire loop', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TestPoint.3dshapes/TestPoint_Bridge_Pitch6.35mm_Drill1.3mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('TestPoint : TestPoint_Bridge_Pitch6.35mm_Drill1.3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

