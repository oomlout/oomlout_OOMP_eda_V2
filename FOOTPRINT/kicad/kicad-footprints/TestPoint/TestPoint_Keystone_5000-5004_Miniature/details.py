
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TestPoint"
    oIndex = "TestPoint_Keystone_5000-5004_Miniature"
    hexID = "FZKTPTPKEYSTONE554MATURE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TestPoint_Keystone_5000-5004_Miniature', 'description': 'Keystone Miniature THM Test Point 5000-5004, http://www.keyelco.com/product-pdf.cfm?p=1309', 'tags': 'Through Hole Mount Test Points', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TestPoint.3dshapes/TestPoint_Keystone_5000-5004_Miniature.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('TestPoint : TestPoint_Keystone_5000-5004_Miniature')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

