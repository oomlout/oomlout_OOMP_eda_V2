
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_L12.6mm_W12.6mm_Px9.52mm_Py9.52mm_Pulse_LP-37"
    hexID = "FZKINLRL126W126PX952PY952PULSELP37"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_L12.6mm_W12.6mm_Px9.52mm_Py9.52mm_Pulse_LP-37', 'description': 'Inductor, Radial series, Radial, pin pitch=9.52*9.52mm^2, , length*width=12.57*12.57mm^2, Pulse, LP-37, http://datasheet.octopart.com/PE-54044NL-Pulse-datasheet-5313493.pdf', 'tags': 'Inductor Radial series Radial pin pitch 9.52*9.52mm^2  length 12.57mm width 12.57mm Pulse LP-37', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_L12.6mm_W12.6mm_Px9.52mm_Py9.52mm_Pulse_LP-37.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_L12.6mm_W12.6mm_Px9.52mm_Py9.52mm_Pulse_LP-37')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

