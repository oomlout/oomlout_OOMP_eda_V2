
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L22.4mm_W10.2mm_P7.90mm_Vishay_TJ4"
    hexID = "FZKINLTOROIDVERTICALL224W12P79VISHAYTJ4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L22.4mm_W10.2mm_P7.90mm_Vishay_TJ4', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=7.90mm, , length*width=22.4*10.2mm^2, Vishay, TJ4, http://www.vishay.com/docs/34079/tj.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 7.90mm  length 22.4mm width 10.2mm Vishay TJ4', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L22.4mm_W10.2mm_P7.90mm_Vishay_TJ4.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L22.4mm_W10.2mm_P7.90mm_Vishay_TJ4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

