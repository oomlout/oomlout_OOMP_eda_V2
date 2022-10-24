
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TestPoint"
    oIndex = "TestPoint_Keystone_5015_Micro-Minature"
    hexID = "FZKTPTPKEYSTONE515INATURE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TestPoint_Keystone_5015_Micro-Minature', 'description': 'SMT Test Point- Micro Miniature 5015, http://www.keyelco.com/product-pdf.cfm?p=1353', 'tags': 'Test Point', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TestPoint.3dshapes/TestPoint_Keystone_5015_Micro-Minature.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('TestPoint : TestPoint_Keystone_5015_Micro-Minature')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

