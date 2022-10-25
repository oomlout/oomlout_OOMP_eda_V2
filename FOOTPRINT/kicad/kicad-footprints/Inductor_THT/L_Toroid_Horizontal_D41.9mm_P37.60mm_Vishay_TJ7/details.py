
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D41.9mm_P37.60mm_Vishay_TJ7"
    hexID = "FZKINLTOROIDHORIZONTALD419P376VISHAYTJ7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D41.9mm_P37.60mm_Vishay_TJ7', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=37.60mm, , diameter=41.9mm, Vishay, TJ7, http://www.vishay.com/docs/34079/tj.pdf', 'tags': 'L_Toroid Horizontal series Radial pin pitch 37.60mm  diameter 41.9mm Vishay TJ7', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D41.9mm_P37.60mm_Vishay_TJ7.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D41.9mm_P37.60mm_Vishay_TJ7')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

