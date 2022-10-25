
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L13.0mm_D4.5mm_P15.24mm_Horizontal_Fastron_HCCC"
    hexID = "FZKINLAXIALL13D45P1524HORIZONTALFASTRONHCCC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L13.0mm_D4.5mm_P15.24mm_Horizontal_Fastron_HCCC', 'description': 'Inductor, Axial series, Axial, Horizontal, pin pitch=15.24mm, , length*diameter=13*4.5mm^2, Fastron, HCCC, http://www.fastrongroup.com/image-show/19/HCCC.pdf?type=Complete-DataSheet&productType=series', 'tags': 'Inductor Axial series Axial Horizontal pin pitch 15.24mm  length 13mm diameter 4.5mm Fastron HCCC', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L13.0mm_D4.5mm_P15.24mm_Horizontal_Fastron_HCCC.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L13.0mm_D4.5mm_P15.24mm_Horizontal_Fastron_HCCC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

