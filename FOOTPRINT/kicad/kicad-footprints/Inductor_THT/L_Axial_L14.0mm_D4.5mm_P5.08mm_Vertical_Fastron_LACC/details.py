
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L14.0mm_D4.5mm_P5.08mm_Vertical_Fastron_LACC"
    hexID = "FZKINLAXIALL14D45P58VERTICALFASTRONLACC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L14.0mm_D4.5mm_P5.08mm_Vertical_Fastron_LACC', 'description': 'Inductor, Axial series, Axial, Vertical, pin pitch=5.08mm, , length*diameter=14*4.5mm^2, Fastron, LACC, http://www.fastrongroup.com/image-show/20/LACC.pdf?type=Complete-DataSheet&productType=series', 'tags': 'Inductor Axial series Axial Vertical pin pitch 5.08mm  length 14mm diameter 4.5mm Fastron LACC', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L14.0mm_D4.5mm_P5.08mm_Vertical_Fastron_LACC.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L14.0mm_D4.5mm_P5.08mm_Vertical_Fastron_LACC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

