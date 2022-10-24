
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D7.8mm_P13.00mm_Diameter9-5mm_Amidon-T30"
    hexID = "FZKINLTOROIDHORIZONTALD78P13DIAMETER95AMIDONT3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D7.8mm_P13.00mm_Diameter9-5mm_Amidon-T30', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=13.00mm, , diameter=7.7978mm, Diameter9-5mm, Amidon-T30', 'tags': 'L_Toroid Horizontal series Radial pin pitch 13.00mm  diameter 7.7978mm Diameter9-5mm Amidon-T30', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D7.8mm_P13.00mm_Diameter9-5mm_Amidon-T30.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D7.8mm_P13.00mm_Diameter9-5mm_Amidon-T30')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

