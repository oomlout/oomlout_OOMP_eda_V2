
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L16.0mm_D9.5mm_P5.08mm_Vertical_Vishay_IM-10-37"
    hexID = "FZKINLAXIALL16D95P58VERTICALVISHAYIM137"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L16.0mm_D9.5mm_P5.08mm_Vertical_Vishay_IM-10-37', 'description': 'Inductor, Axial series, Axial, Vertical, pin pitch=5.08mm, , length*diameter=16*9.5mm^2, Vishay, IM-10-37, http://www.vishay.com/docs/34030/im10.pdf', 'tags': 'Inductor Axial series Axial Vertical pin pitch 5.08mm  length 16mm diameter 9.5mm Vishay IM-10-37', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L16.0mm_D9.5mm_P5.08mm_Vertical_Vishay_IM-10-37.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L16.0mm_D9.5mm_P5.08mm_Vertical_Vishay_IM-10-37')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

