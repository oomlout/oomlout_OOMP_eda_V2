
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Filter"
    oIndex = "Filter_Mini-Circuits_FV1206-4"
    hexID = "FZKFILFILMCIRCUITSFV1264"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Filter_Mini-Circuits_FV1206-4', 'description': 'Mini-Circuits Filter SMD 1206 https://ww2.minicircuits.com/case_style/FV1206-4.pdf', 'tags': 'Mini-Circuits Filter SMD 1206', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Filter.3dshapes/Filter_Mini-Circuits_FV1206-4.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Filter : Filter_Mini-Circuits_FV1206-4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

