
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L12.8mm_D5.8mm_P7.62mm_Vertical_Fastron_HBCC"
    hexID = "FZKINLAXIALL128D58P762VERTICALFASTRONHBCC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L12.8mm_D5.8mm_P7.62mm_Vertical_Fastron_HBCC', 'description': 'Inductor, Axial series, Axial, Vertical, pin pitch=7.62mm, , length*diameter=12.8*5.8mm^2, Fastron, HBCC, http://www.fastrongroup.com/image-show/18/HBCC.pdf?type=Complete-DataSheet&productType=series', 'tags': 'Inductor Axial series Axial Vertical pin pitch 7.62mm  length 12.8mm diameter 5.8mm Fastron HBCC', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L12.8mm_D5.8mm_P7.62mm_Vertical_Fastron_HBCC.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L12.8mm_D5.8mm_P7.62mm_Vertical_Fastron_HBCC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

