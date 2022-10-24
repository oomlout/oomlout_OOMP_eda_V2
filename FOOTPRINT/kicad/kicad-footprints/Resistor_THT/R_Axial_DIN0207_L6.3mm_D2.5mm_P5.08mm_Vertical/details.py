
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Axial_DIN0207_L6.3mm_D2.5mm_P5.08mm_Vertical"
    hexID = "FZKRRAXIALDIN27L63D25P58VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Axial_DIN0207_L6.3mm_D2.5mm_P5.08mm_Vertical', 'description': 'Resistor, Axial_DIN0207 series, Axial, Vertical, pin pitch=5.08mm, 0.25W = 1/4W, length*diameter=6.3*2.5mm^2, http://cdn-reichelt.de/documents/datenblatt/B400/1_4W%23YAG.pdf', 'tags': 'Resistor Axial_DIN0207 series Axial Vertical pin pitch 5.08mm 0.25W = 1/4W length 6.3mm diameter 2.5mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_DIN0207_L6.3mm_D2.5mm_P5.08mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Axial_DIN0207_L6.3mm_D2.5mm_P5.08mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

