
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Filter"
    oIndex = "Filter_Mini-Circuits_FV1206-5"
    hexID = "FZKFILFILMCIRCUITSFV1265"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Filter_Mini-Circuits_FV1206-5', 'description': 'Mini-Circuits Filter SMD 1206 https://ww2.minicircuits.com/case_style/FV1206-5.pdf', 'tags': 'Mini-Circuits Filter SMD 1206', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Filter.3dshapes/Filter_Mini-Circuits_FV1206-5.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Filter : Filter_Mini-Circuits_FV1206-5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

