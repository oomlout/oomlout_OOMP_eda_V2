
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L12.0mm_D5.0mm_P15.24mm_Horizontal_Fastron_MISC"
    hexID = "FZKINLAXIALL12D5P1524HORIZONTALFASTRONMISC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L12.0mm_D5.0mm_P15.24mm_Horizontal_Fastron_MISC', 'description': 'Inductor, Axial series, Axial, Horizontal, pin pitch=15.24mm, , length*diameter=12*5mm^2, Fastron, MISC, http://cdn-reichelt.de/documents/datenblatt/B400/DS_MISC.pdf', 'tags': 'Inductor Axial series Axial Horizontal pin pitch 15.24mm  length 12mm diameter 5mm Fastron MISC', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L12.0mm_D5.0mm_P15.24mm_Horizontal_Fastron_MISC.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L12.0mm_D5.0mm_P15.24mm_Horizontal_Fastron_MISC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

