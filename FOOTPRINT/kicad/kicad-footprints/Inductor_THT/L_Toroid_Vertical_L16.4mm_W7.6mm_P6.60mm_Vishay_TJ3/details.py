
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L16.4mm_W7.6mm_P6.60mm_Vishay_TJ3"
    hexID = "FZKINLTOROIDVERTICALL164W76P66VISHAYTJ3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L16.4mm_W7.6mm_P6.60mm_Vishay_TJ3', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=6.60mm, , length*width=16.4*7.6mm^2, Vishay, TJ3, http://www.vishay.com/docs/34079/tj.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 6.60mm  length 16.4mm width 7.6mm Vishay TJ3', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L16.4mm_W7.6mm_P6.60mm_Vishay_TJ3.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L16.4mm_W7.6mm_P6.60mm_Vishay_TJ3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

