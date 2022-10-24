
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L30.0mm_D8.0mm_P35.56mm_Horizontal_Fastron_77A"
    hexID = "FZKINLAXIALL3D8P3556HORIZONTALFASTRON77A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L30.0mm_D8.0mm_P35.56mm_Horizontal_Fastron_77A', 'description': 'Inductor, Axial series, Axial, Horizontal, pin pitch=35.56mm, , length*diameter=30*8mm^2, Fastron, 77A, http://cdn-reichelt.de/documents/datenblatt/B400/DS_77A.pdf', 'tags': 'Inductor Axial series Axial Horizontal pin pitch 35.56mm  length 30mm diameter 8mm Fastron 77A', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L30.0mm_D8.0mm_P35.56mm_Horizontal_Fastron_77A.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L30.0mm_D8.0mm_P35.56mm_Horizontal_Fastron_77A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

