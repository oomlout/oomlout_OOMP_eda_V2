
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D16.8mm_P14.70mm_Vishay_TJ3_BigPads"
    hexID = "FZKINLTOROIDHORIZONTALD168P147VISHAYTJ3BIGPADS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D16.8mm_P14.70mm_Vishay_TJ3_BigPads', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=14.70mm, , diameter=16.8mm, Vishay, TJ3, BigPads, http://www.vishay.com/docs/34079/tj.pdf', 'tags': 'L_Toroid Horizontal series Radial pin pitch 14.70mm  diameter 16.8mm Vishay TJ3 BigPads', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D16.8mm_P14.70mm_Vishay_TJ3_BigPads.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D16.8mm_P14.70mm_Vishay_TJ3_BigPads')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

