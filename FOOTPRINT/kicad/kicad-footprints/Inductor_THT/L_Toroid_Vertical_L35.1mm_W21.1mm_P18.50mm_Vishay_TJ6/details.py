
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L35.1mm_W21.1mm_P18.50mm_Vishay_TJ6"
    hexID = "FZKINLTOROIDVERTICALL351W211P185VISHAYTJ6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L35.1mm_W21.1mm_P18.50mm_Vishay_TJ6', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=18.50mm, , length*width=35.1*21.1mm^2, Vishay, TJ6, http://www.vishay.com/docs/34079/tj.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 18.50mm  length 35.1mm width 21.1mm Vishay TJ6', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L35.1mm_W21.1mm_P18.50mm_Vishay_TJ6.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L35.1mm_W21.1mm_P18.50mm_Vishay_TJ6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

