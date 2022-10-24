
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D22.4mm_P19.80mm_Vishay_TJ4"
    hexID = "FZKINLTOROIDHORIZONTALD224P198VISHAYTJ4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D22.4mm_P19.80mm_Vishay_TJ4', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=19.80mm, , diameter=22.4mm, Vishay, TJ4, http://www.vishay.com/docs/34079/tj.pdf', 'tags': 'L_Toroid Horizontal series Radial pin pitch 19.80mm  diameter 22.4mm Vishay TJ4', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D22.4mm_P19.80mm_Vishay_TJ4.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D22.4mm_P19.80mm_Vishay_TJ4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

