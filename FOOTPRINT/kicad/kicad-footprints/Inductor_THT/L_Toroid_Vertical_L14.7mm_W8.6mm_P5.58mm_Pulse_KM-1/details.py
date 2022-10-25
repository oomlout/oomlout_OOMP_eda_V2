
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L14.7mm_W8.6mm_P5.58mm_Pulse_KM-1"
    hexID = "FZKINLTOROIDVERTICALL147W86P558PULSEKM1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L14.7mm_W8.6mm_P5.58mm_Pulse_KM-1', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=5.58mm, , length*width=14.73*8.64mm^2, Pulse, KM-1, http://datasheet.octopart.com/PE-92112KNL-Pulse-datasheet-17853305.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 5.58mm  length 14.73mm width 8.64mm Pulse KM-1', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L14.7mm_W8.6mm_P5.58mm_Pulse_KM-1.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L14.7mm_W8.6mm_P5.58mm_Pulse_KM-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

