
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Mini-Circuits"
    oIndex = "Mini-Circuits_MMM168_LandPatternPL-225"
    hexID = "FZKRFMCIRCUITSM168LANDPATTERNPL225"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mini-Circuits_MMM168_LandPatternPL-225', 'description': 'Footprint for Mini-Circuits case MMM168, Land pattern PL-225, vias included, (case drawing: https://ww2.minicircuits.com/case_style/MMM168.pdf, land pattern drawing: https://ww2.minicircuits.com/pcb/98-pl225.pdf)', 'tags': 'pl-225', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Mini-Circuits.3dshapes/Mini-Circuits_MMM168.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Mini-Circuits : Mini-Circuits_MMM168_LandPatternPL-225')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

