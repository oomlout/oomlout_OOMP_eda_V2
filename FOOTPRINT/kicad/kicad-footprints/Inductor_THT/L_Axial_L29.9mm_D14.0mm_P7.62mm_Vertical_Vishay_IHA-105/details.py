
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L29.9mm_D14.0mm_P7.62mm_Vertical_Vishay_IHA-105"
    hexID = "FZKINLAXIALL299D14P762VERTICALVISHAYIHA15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L29.9mm_D14.0mm_P7.62mm_Vertical_Vishay_IHA-105', 'description': 'Inductor, Axial series, Axial, Vertical, pin pitch=7.62mm, , length*diameter=29.85*13.97mm^2, Vishay, IHA-105, http://www.vishay.com/docs/34014/iha.pdf', 'tags': 'Inductor Axial series Axial Vertical pin pitch 7.62mm  length 29.85mm diameter 13.97mm Vishay IHA-105', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L29.9mm_D14.0mm_P7.62mm_Vertical_Vishay_IHA-105.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L29.9mm_D14.0mm_P7.62mm_Vertical_Vishay_IHA-105')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

