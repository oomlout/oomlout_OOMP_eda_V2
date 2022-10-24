
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D9.5mm_P15.00mm_Diameter10-5mm_Amidon-T37"
    hexID = "FZKINLTOROIDHORIZONTALD95P15DIAMETER15AMIDONT37"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D9.5mm_P15.00mm_Diameter10-5mm_Amidon-T37', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=15.00mm, , diameter=9.524999999999999mm, Diameter10-5mm, Amidon-T37', 'tags': 'L_Toroid Horizontal series Radial pin pitch 15.00mm  diameter 9.524999999999999mm Diameter10-5mm Amidon-T37', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D9.5mm_P15.00mm_Diameter10-5mm_Amidon-T37.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D9.5mm_P15.00mm_Diameter10-5mm_Amidon-T37')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

