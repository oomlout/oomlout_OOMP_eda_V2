
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Mini-Circuits"
    oIndex = "Mini-Circuits_GP731_LandPatternPL-176"
    hexID = "FZKRFMCIRCUITSGP731LANDPATTERNPL176"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mini-Circuits_GP731_LandPatternPL-176', 'description': 'Footprint for Mini-Circuits case GP731 (https://ww2.minicircuits.com/case_style/GP731.pdf) following land pattern PL-176, including GND vias (https://www.minicircuits.com/pcb/98-pl176.pdf)', 'tags': 'mini-circuits PL-176', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Mini-Circuits.3dshapes/Mini-Circuits_GP731.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('RF_Mini-Circuits : Mini-Circuits_GP731_LandPatternPL-176')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

