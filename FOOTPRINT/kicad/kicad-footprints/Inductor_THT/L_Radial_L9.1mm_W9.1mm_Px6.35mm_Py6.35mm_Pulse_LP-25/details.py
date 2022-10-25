
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_L9.1mm_W9.1mm_Px6.35mm_Py6.35mm_Pulse_LP-25"
    hexID = "FZKINLRL91W91PX635PY635PULSELP25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_L9.1mm_W9.1mm_Px6.35mm_Py6.35mm_Pulse_LP-25', 'description': 'Inductor, Radial series, Radial, pin pitch=6.35*6.35mm^2, , length*width=9.14*9.14mm^2, Pulse, LP-25, http://datasheet.octopart.com/PE-54044NL-Pulse-datasheet-5313493.pdf', 'tags': 'Inductor Radial series Radial pin pitch 6.35*6.35mm^2  length 9.14mm width 9.14mm Pulse LP-25', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_L9.1mm_W9.1mm_Px6.35mm_Py6.35mm_Pulse_LP-25.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_L9.1mm_W9.1mm_Px6.35mm_Py6.35mm_Pulse_LP-25')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

