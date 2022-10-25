
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L16.0mm_W8.0mm_P7.62mm"
    hexID = "FZKINLTOROIDVERTICALL16W8P762"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L16.0mm_W8.0mm_P7.62mm', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=7.62mm, , length*width=16*8mm^2', 'tags': 'L_Toroid Vertical series Radial pin pitch 7.62mm  length 16mm width 8mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L16.0mm_W8.0mm_P7.62mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L16.0mm_W8.0mm_P7.62mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

