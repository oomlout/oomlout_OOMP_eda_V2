
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L17.8mm_W9.7mm_P7.11mm_Pulse_B"
    hexID = "FZKINLTOROIDVERTICALL178W97P711PULSEB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L17.8mm_W9.7mm_P7.11mm_Pulse_B', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=7.11mm, , length*width=17.78*9.65mm^2, Pulse, B, http://datasheet.octopart.com/PE-92112KNL-Pulse-datasheet-17853305.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 7.11mm  length 17.78mm width 9.65mm Pulse B', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L17.8mm_W9.7mm_P7.11mm_Pulse_B.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L17.8mm_W9.7mm_P7.11mm_Pulse_B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

