
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L11.0mm_D4.5mm_P15.24mm_Horizontal_Fastron_MECC"
    hexID = "FZKINLAXIALL11D45P1524HORIZONTALFASTRONMECC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L11.0mm_D4.5mm_P15.24mm_Horizontal_Fastron_MECC', 'description': 'Inductor, Axial series, Axial, Horizontal, pin pitch=15.24mm, , length*diameter=11*4.5mm^2, Fastron, MECC, http://www.fastrongroup.com/image-show/21/MECC.pdf?type=Complete-DataSheet&productType=series', 'tags': 'Inductor Axial series Axial Horizontal pin pitch 15.24mm  length 11mm diameter 4.5mm Fastron MECC', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L11.0mm_D4.5mm_P15.24mm_Horizontal_Fastron_MECC.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L11.0mm_D4.5mm_P15.24mm_Horizontal_Fastron_MECC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

