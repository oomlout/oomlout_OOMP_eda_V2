
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L13.0mm_W6.5mm_P5.60mm"
    hexID = "FZKINLTOROIDVERTICALL13W65P56"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L13.0mm_W6.5mm_P5.60mm', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=5.60mm, , length*width=13*6.5mm^2', 'tags': 'L_Toroid Vertical series Radial pin pitch 5.60mm  length 13mm width 6.5mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L13.0mm_W6.5mm_P5.60mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L13.0mm_W6.5mm_P5.60mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

