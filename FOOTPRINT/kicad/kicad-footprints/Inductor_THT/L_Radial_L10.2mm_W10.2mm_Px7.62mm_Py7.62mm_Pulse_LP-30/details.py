
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_L10.2mm_W10.2mm_Px7.62mm_Py7.62mm_Pulse_LP-30"
    hexID = "FZKINLRL12W12PX762PY762PULSELP3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_L10.2mm_W10.2mm_Px7.62mm_Py7.62mm_Pulse_LP-30', 'description': 'Inductor, Radial series, Radial, pin pitch=7.62*7.62mm^2, , length*width=10.16*10.16mm^2, Pulse, LP-30, http://datasheet.octopart.com/PE-54044NL-Pulse-datasheet-5313493.pdf', 'tags': 'Inductor Radial series Radial pin pitch 7.62*7.62mm^2  length 10.16mm width 10.16mm Pulse LP-30', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_L10.2mm_W10.2mm_Px7.62mm_Py7.62mm_Pulse_LP-30.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_L10.2mm_W10.2mm_Px7.62mm_Py7.62mm_Pulse_LP-30')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

