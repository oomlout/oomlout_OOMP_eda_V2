
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Mini-Circuits"
    oIndex = "Mini-Circuits_BK377_LandPatternPL-005"
    hexID = "FZKRFMCIRCUITSBK377LANDPATTERNPL5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mini-Circuits_BK377_LandPatternPL-005', 'description': 'Footprint for Mini-Circuits case BK377 (https://ww2.minicircuits.com/case_style/BK276.pdf) according to land-pattern PL-005, including GND vias (https://ww2.minicircuits.com/pcb/98-pl005.pdf)', 'tags': 'Mini-circuits VCXO JTOS PL-005', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Mini-Circuits.3dshapes/Mini-Circuits_BK377.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('RF_Mini-Circuits : Mini-Circuits_BK377_LandPatternPL-005')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

