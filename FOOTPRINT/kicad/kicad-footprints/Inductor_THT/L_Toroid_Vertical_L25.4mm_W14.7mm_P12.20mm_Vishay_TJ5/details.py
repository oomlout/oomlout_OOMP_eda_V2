
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L25.4mm_W14.7mm_P12.20mm_Vishay_TJ5"
    hexID = "FZKINLTOROIDVERTICALL254W147P122VISHAYTJ5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L25.4mm_W14.7mm_P12.20mm_Vishay_TJ5', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=12.20mm, , length*width=25.4*14.7mm^2, Vishay, TJ5, http://www.vishay.com/docs/34079/tj.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 12.20mm  length 25.4mm width 14.7mm Vishay TJ5', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L25.4mm_W14.7mm_P12.20mm_Vishay_TJ5.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L25.4mm_W14.7mm_P12.20mm_Vishay_TJ5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

