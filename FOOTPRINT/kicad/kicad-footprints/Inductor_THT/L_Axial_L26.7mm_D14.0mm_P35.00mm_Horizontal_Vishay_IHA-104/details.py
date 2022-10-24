
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L26.7mm_D14.0mm_P35.00mm_Horizontal_Vishay_IHA-104"
    hexID = "FZKINLAXIALL267D14P35HORIZONTALVISHAYIHA14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L26.7mm_D14.0mm_P35.00mm_Horizontal_Vishay_IHA-104', 'description': 'Inductor, Axial series, Axial, Horizontal, pin pitch=35mm, , length*diameter=26.67*13.97mm^2, Vishay, IHA-104, http://www.vishay.com/docs/34014/iha.pdf', 'tags': 'Inductor Axial series Axial Horizontal pin pitch 35mm  length 26.67mm diameter 13.97mm Vishay IHA-104', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L26.7mm_D14.0mm_P35.00mm_Horizontal_Vishay_IHA-104.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L26.7mm_D14.0mm_P35.00mm_Horizontal_Vishay_IHA-104')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

