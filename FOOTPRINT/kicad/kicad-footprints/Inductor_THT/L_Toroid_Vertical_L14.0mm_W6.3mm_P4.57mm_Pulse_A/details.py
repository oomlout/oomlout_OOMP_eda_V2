
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L14.0mm_W6.3mm_P4.57mm_Pulse_A"
    hexID = "FZKINLTOROIDVERTICALL14W63P457PULSEA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L14.0mm_W6.3mm_P4.57mm_Pulse_A', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=4.57mm, , length*width=13.97*6.35mm^2, Pulse, A, http://datasheet.octopart.com/PE-92112KNL-Pulse-datasheet-17853305.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 4.57mm  length 13.97mm width 6.35mm Pulse A', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L14.0mm_W6.3mm_P4.57mm_Pulse_A.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L14.0mm_W6.3mm_P4.57mm_Pulse_A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

