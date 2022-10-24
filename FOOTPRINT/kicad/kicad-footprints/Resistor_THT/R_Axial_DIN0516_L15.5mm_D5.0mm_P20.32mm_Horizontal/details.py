
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Axial_DIN0516_L15.5mm_D5.0mm_P20.32mm_Horizontal"
    hexID = "FZKRRAXIALDIN516L155D5P232HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Axial_DIN0516_L15.5mm_D5.0mm_P20.32mm_Horizontal', 'description': 'Resistor, Axial_DIN0516 series, Axial, Horizontal, pin pitch=20.32mm, 2W, length*diameter=15.5*5mm^2, http://cdn-reichelt.de/documents/datenblatt/B400/1_4W%23YAG.pdf', 'tags': 'Resistor Axial_DIN0516 series Axial Horizontal pin pitch 20.32mm 2W length 15.5mm diameter 5mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_DIN0516_L15.5mm_D5.0mm_P20.32mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Axial_DIN0516_L15.5mm_D5.0mm_P20.32mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

