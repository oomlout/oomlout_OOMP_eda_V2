
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L41.9mm_W17.8mm_P12.70mm_Pulse_F"
    hexID = "FZKINLTOROIDVERTICALL419W178P127PULSEF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L41.9mm_W17.8mm_P12.70mm_Pulse_F', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=12.70mm, , length*width=41.91*17.78mm^2, Pulse, F, http://datasheet.octopart.com/PE-92112KNL-Pulse-datasheet-17853305.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 12.70mm  length 41.91mm width 17.78mm Pulse F', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L41.9mm_W17.8mm_P12.70mm_Pulse_F.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L41.9mm_W17.8mm_P12.70mm_Pulse_F')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

