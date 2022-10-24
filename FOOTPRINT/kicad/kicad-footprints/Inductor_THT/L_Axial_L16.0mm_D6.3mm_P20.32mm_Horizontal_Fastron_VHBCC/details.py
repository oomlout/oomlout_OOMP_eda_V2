
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L16.0mm_D6.3mm_P20.32mm_Horizontal_Fastron_VHBCC"
    hexID = "FZKINLAXIALL16D63P232HORIZONTALFASTRONVHBCC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L16.0mm_D6.3mm_P20.32mm_Horizontal_Fastron_VHBCC', 'description': 'Inductor, Axial series, Axial, Horizontal, pin pitch=20.32mm, , length*diameter=16*6.3mm^2, Fastron, VHBCC, http://www.fastrongroup.com/image-show/25/VHBCC.pdf?type=Complete-DataSheet&productType=series', 'tags': 'Inductor Axial series Axial Horizontal pin pitch 20.32mm  length 16mm diameter 6.3mm Fastron VHBCC', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L16.0mm_D6.3mm_P20.32mm_Horizontal_Fastron_VHBCC.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L16.0mm_D6.3mm_P20.32mm_Horizontal_Fastron_VHBCC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

