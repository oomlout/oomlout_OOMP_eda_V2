
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D35.1mm_P31.00mm_Vishay_TJ6"
    hexID = "FZKINLTOROIDHORIZONTALD351P31VISHAYTJ6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D35.1mm_P31.00mm_Vishay_TJ6', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=31.00mm, , diameter=35.1mm, Vishay, TJ6, http://www.vishay.com/docs/34079/tj.pdf', 'tags': 'L_Toroid Horizontal series Radial pin pitch 31.00mm  diameter 35.1mm Vishay TJ6', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D35.1mm_P31.00mm_Vishay_TJ6.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D35.1mm_P31.00mm_Vishay_TJ6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

