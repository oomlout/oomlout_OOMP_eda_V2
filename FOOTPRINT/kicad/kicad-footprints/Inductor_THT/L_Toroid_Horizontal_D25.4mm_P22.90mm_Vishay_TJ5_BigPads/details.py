
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D25.4mm_P22.90mm_Vishay_TJ5_BigPads"
    hexID = "FZKINLTOROIDHORIZONTALD254P229VISHAYTJ5BIGPADS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D25.4mm_P22.90mm_Vishay_TJ5_BigPads', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=22.90mm, , diameter=25.4mm, Vishay, TJ5, BigPads, http://www.vishay.com/docs/34079/tj.pdf', 'tags': 'L_Toroid Horizontal series Radial pin pitch 22.90mm  diameter 25.4mm Vishay TJ5 BigPads', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D25.4mm_P22.90mm_Vishay_TJ5_BigPads.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D25.4mm_P22.90mm_Vishay_TJ5_BigPads')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

