
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L9.5mm_D4.0mm_P2.54mm_Vertical_Fastron_SMCC"
    hexID = "FZKINLAXIALL95D4P254VERTICALFASTRONSMCC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L9.5mm_D4.0mm_P2.54mm_Vertical_Fastron_SMCC', 'description': 'Inductor, Axial series, Axial, Vertical, pin pitch=2.54mm, , length*diameter=9.5*4mm^2, Fastron, SMCC, http://cdn-reichelt.de/documents/datenblatt/B400/DS_SMCC_NEU.pdf, http://cdn-reichelt.de/documents/datenblatt/B400/LEADEDINDUCTORS.pdf', 'tags': 'Inductor Axial series Axial Vertical pin pitch 2.54mm  length 9.5mm diameter 4mm Fastron SMCC', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L9.5mm_D4.0mm_P2.54mm_Vertical_Fastron_SMCC.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L9.5mm_D4.0mm_P2.54mm_Vertical_Fastron_SMCC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

