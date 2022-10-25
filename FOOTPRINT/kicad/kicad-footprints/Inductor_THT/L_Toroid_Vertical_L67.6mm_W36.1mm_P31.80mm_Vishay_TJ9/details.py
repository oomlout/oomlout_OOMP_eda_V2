
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L67.6mm_W36.1mm_P31.80mm_Vishay_TJ9"
    hexID = "FZKINLTOROIDVERTICALL676W361P318VISHAYTJ9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L67.6mm_W36.1mm_P31.80mm_Vishay_TJ9', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=31.80mm, , length*width=67.6*36.1mm^2, Vishay, TJ9, http://www.vishay.com/docs/34079/tj.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 31.80mm  length 67.6mm width 36.1mm Vishay TJ9', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L67.6mm_W36.1mm_P31.80mm_Vishay_TJ9.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L67.6mm_W36.1mm_P31.80mm_Vishay_TJ9')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

