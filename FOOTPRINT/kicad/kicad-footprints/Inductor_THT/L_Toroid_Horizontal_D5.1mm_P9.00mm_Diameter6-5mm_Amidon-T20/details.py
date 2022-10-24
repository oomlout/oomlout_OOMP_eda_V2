
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D5.1mm_P9.00mm_Diameter6-5mm_Amidon-T20"
    hexID = "FZKINLTOROIDHORIZONTALD51P9DIAMETER65AMIDONT2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D5.1mm_P9.00mm_Diameter6-5mm_Amidon-T20', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=9.00mm, , diameter=5.08mm, Diameter6-5mm, Amidon-T20', 'tags': 'L_Toroid Horizontal series Radial pin pitch 9.00mm  diameter 5.08mm Diameter6-5mm Amidon-T20', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D5.1mm_P9.00mm_Diameter6-5mm_Amidon-T20.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D5.1mm_P9.00mm_Diameter6-5mm_Amidon-T20')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

