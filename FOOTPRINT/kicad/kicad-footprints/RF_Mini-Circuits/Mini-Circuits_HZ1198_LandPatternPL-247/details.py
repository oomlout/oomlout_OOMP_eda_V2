
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Mini-Circuits"
    oIndex = "Mini-Circuits_HZ1198_LandPatternPL-247"
    hexID = "FZKRFMCIRCUITSHZ1198LANDPATTERNPL247"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mini-Circuits_HZ1198_LandPatternPL-247', 'description': 'Footprint for Mini-Circuits cas HZ1198 (https://ww2.minicircuits.com/case_style/HZ1198.pdf) following land pattern PL-247, including GND-vias (https://www.minicircuits.com/pcb/98-pl247.pdf)', 'tags': 'Mini-Circuits PL-247 HZ1198', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Mini-Circuits.3dshapes/Mini-Circuits_HZ1198.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Mini-Circuits : Mini-Circuits_HZ1198_LandPatternPL-247')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

