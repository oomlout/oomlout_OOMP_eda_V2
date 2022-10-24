
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Mini-Circuits"
    oIndex = "Mini-Circuits_CK605_LandPatternPL-012"
    hexID = "FZKRFMCIRCUITSCK65LANDPATTERNPL12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mini-Circuits_CK605_LandPatternPL-012', 'description': 'Footprint for Mini-Circuits case CK605 (https://ww2.minicircuits.com/case_style/CK605.pdf) following land pattern PL-012, including GND vias (https://ww2.minicircuits.com/pcb/98-pl012.pdf)', 'tags': 'Mini-Circuits PL-012', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Mini-Circuits.3dshapes/Mini-Circuits_CK605.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Mini-Circuits : Mini-Circuits_CK605_LandPatternPL-012')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

