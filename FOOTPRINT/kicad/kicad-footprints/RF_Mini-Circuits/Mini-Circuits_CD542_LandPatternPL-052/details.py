
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Mini-Circuits"
    oIndex = "Mini-Circuits_CD542_LandPatternPL-052"
    hexID = "FZKRFMCIRCUITSCD542LANDPATTERNPL52"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mini-Circuits_CD542_LandPatternPL-052', 'description': 'Footprint for Mini-Circuits case CD542 (https://ww2.minicircuits.com/case_style/CD542.pdf) using land-pattern PL-052, including GND-vias (https://ww2.minicircuits.com/pcb/98-pl052.pdf)', 'tags': 'MiniCircuits PL-052 CD542', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Mini-Circuits.3dshapes/Mini-Circuits_CD542.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('RF_Mini-Circuits : Mini-Circuits_CD542_LandPatternPL-052')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

