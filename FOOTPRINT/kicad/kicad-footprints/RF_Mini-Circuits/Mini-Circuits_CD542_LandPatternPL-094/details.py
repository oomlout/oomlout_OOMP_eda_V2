
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Mini-Circuits"
    oIndex = "Mini-Circuits_CD542_LandPatternPL-094"
    hexID = "FZKRFMCIRCUITSCD542LANDPATTERNPL94"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mini-Circuits_CD542_LandPatternPL-094', 'description': 'Footprint for mini circuit case CD542, Land pattern PL-094, pads 5 and 2 connected via insulated copper area below body, vias included (case drawing: https://ww2.minicircuits.com/case_style/CD542.pdf, land pattern drawing: https://ww2.minicircuits.com/pcb/98-pl094.pdf)', 'tags': 'mini-circuits CD542 pl-094', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Mini-Circuits.3dshapes/Mini-Circuits_CD542.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Mini-Circuits : Mini-Circuits_CD542_LandPatternPL-094')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

