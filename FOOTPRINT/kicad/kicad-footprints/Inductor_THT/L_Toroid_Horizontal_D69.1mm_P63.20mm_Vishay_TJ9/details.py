
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D69.1mm_P63.20mm_Vishay_TJ9"
    hexID = "FZKINLTOROIDHORIZONTALD691P632VISHAYTJ9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D69.1mm_P63.20mm_Vishay_TJ9', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=63.20mm, , diameter=69.1mm, Vishay, TJ9, http://www.vishay.com/docs/34079/tj.pdf', 'tags': 'L_Toroid Horizontal series Radial pin pitch 63.20mm  diameter 69.1mm Vishay TJ9', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D69.1mm_P63.20mm_Vishay_TJ9.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D69.1mm_P63.20mm_Vishay_TJ9')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

