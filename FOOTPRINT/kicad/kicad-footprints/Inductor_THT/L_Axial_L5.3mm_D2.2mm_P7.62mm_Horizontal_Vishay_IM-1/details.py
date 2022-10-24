
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L5.3mm_D2.2mm_P7.62mm_Horizontal_Vishay_IM-1"
    hexID = "FZKINLAXIALL53D22P762HORIZONTALVISHAYIM1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L5.3mm_D2.2mm_P7.62mm_Horizontal_Vishay_IM-1', 'description': 'Inductor, Axial series, Axial, Horizontal, pin pitch=7.62mm, , length*diameter=5.3*2.2mm^2, Vishay, IM-1, http://www.vishay.com/docs/34030/im.pdf', 'tags': 'Inductor Axial series Axial Horizontal pin pitch 7.62mm  length 5.3mm diameter 2.2mm Vishay IM-1', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L5.3mm_D2.2mm_P7.62mm_Horizontal_Vishay_IM-1.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L5.3mm_D2.2mm_P7.62mm_Horizontal_Vishay_IM-1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

