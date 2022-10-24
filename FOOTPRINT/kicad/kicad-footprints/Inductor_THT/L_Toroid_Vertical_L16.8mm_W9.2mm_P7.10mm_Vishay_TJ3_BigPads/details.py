
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L16.8mm_W9.2mm_P7.10mm_Vishay_TJ3_BigPads"
    hexID = "FZKINLTOROIDVERTICALL168W92P71VISHAYTJ3BIGPADS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L16.8mm_W9.2mm_P7.10mm_Vishay_TJ3_BigPads', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=7.10mm, , length*width=16.8*9.2mm^2, Vishay, TJ3, BigPads, http://www.vishay.com/docs/34079/tj.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 7.10mm  length 16.8mm width 9.2mm Vishay TJ3 BigPads', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L16.8mm_W9.2mm_P7.10mm_Vishay_TJ3_BigPads.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L16.8mm_W9.2mm_P7.10mm_Vishay_TJ3_BigPads')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

