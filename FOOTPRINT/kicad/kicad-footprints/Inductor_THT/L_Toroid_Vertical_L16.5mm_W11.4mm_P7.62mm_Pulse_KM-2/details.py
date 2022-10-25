
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L16.5mm_W11.4mm_P7.62mm_Pulse_KM-2"
    hexID = "FZKINLTOROIDVERTICALL165W114P762PULSEKM2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L16.5mm_W11.4mm_P7.62mm_Pulse_KM-2', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=7.62mm, , length*width=16.51*11.43mm^2, Pulse, KM-2, http://datasheet.octopart.com/PE-92112KNL-Pulse-datasheet-17853305.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 7.62mm  length 16.51mm width 11.43mm Pulse KM-2', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L16.5mm_W11.4mm_P7.62mm_Pulse_KM-2.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L16.5mm_W11.4mm_P7.62mm_Pulse_KM-2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

