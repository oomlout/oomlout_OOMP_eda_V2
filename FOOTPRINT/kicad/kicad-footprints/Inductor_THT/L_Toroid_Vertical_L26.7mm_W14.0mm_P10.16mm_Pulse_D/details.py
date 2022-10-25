
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L26.7mm_W14.0mm_P10.16mm_Pulse_D"
    hexID = "FZKINLTOROIDVERTICALL267W14P116PULSED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L26.7mm_W14.0mm_P10.16mm_Pulse_D', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=10.16mm, , length*width=26.67*13.97mm^2, Pulse, D, http://datasheet.octopart.com/PE-92112KNL-Pulse-datasheet-17853305.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 10.16mm  length 26.67mm width 13.97mm Pulse D', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L26.7mm_W14.0mm_P10.16mm_Pulse_D.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L26.7mm_W14.0mm_P10.16mm_Pulse_D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

