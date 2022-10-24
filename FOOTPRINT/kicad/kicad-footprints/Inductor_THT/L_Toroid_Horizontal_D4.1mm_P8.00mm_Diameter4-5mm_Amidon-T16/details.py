
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D4.1mm_P8.00mm_Diameter4-5mm_Amidon-T16"
    hexID = "FZKINLTOROIDHORIZONTALD41P8DIAMETER45AMIDONT16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D4.1mm_P8.00mm_Diameter4-5mm_Amidon-T16', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=8.00mm, , diameter=4.064mm, Diameter4-5mm, Amidon-T16', 'tags': 'L_Toroid Horizontal series Radial pin pitch 8.00mm  diameter 4.064mm Diameter4-5mm Amidon-T16', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D4.1mm_P8.00mm_Diameter4-5mm_Amidon-T16.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D4.1mm_P8.00mm_Diameter4-5mm_Amidon-T16')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

