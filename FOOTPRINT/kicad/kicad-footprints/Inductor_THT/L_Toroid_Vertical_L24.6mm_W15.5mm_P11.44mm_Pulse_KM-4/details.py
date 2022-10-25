
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L24.6mm_W15.5mm_P11.44mm_Pulse_KM-4"
    hexID = "FZKINLTOROIDVERTICALL246W155P1144PULSEKM4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L24.6mm_W15.5mm_P11.44mm_Pulse_KM-4', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=11.44mm, , length*width=24.64*15.5mm^2, Pulse, KM-4, http://datasheet.octopart.com/PE-92112KNL-Pulse-datasheet-17853305.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 11.44mm  length 24.64mm width 15.5mm Pulse KM-4', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L24.6mm_W15.5mm_P11.44mm_Pulse_KM-4.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L24.6mm_W15.5mm_P11.44mm_Pulse_KM-4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

