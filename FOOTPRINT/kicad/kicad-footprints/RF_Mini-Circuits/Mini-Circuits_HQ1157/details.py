
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Mini-Circuits"
    oIndex = "Mini-Circuits_HQ1157"
    hexID = "FZKRFMCIRCUITSHQ1157"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mini-Circuits_HQ1157', 'description': 'Footprint for Mini-Circuits case HQ1157 (https://www.minicircuits.com/case_style/HQ1157.pdf)', 'tags': 'Mini-Circuits HQ1157', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Mini-Circuits.3dshapes/Mini-Circuits_HQ1157.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Mini-Circuits : Mini-Circuits_HQ1157')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

