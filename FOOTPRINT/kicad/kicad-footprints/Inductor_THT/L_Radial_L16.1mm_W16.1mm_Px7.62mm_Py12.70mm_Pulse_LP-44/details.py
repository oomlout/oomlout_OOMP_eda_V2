
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_L16.1mm_W16.1mm_Px7.62mm_Py12.70mm_Pulse_LP-44"
    hexID = "FZKINLRL161W161PX762PY127PULSELP44"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_L16.1mm_W16.1mm_Px7.62mm_Py12.70mm_Pulse_LP-44', 'description': 'Inductor, Radial series, Radial, pin pitch=7.62*12.70mm^2, , length*width=16.13*16.13mm^2, Pulse, LP-44, http://datasheet.octopart.com/PE-54044NL-Pulse-datasheet-5313493.pdf', 'tags': 'Inductor Radial series Radial pin pitch 7.62*12.70mm^2  length 16.13mm width 16.13mm Pulse LP-44', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_L16.1mm_W16.1mm_Px7.62mm_Py12.70mm_Pulse_LP-44.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_L16.1mm_W16.1mm_Px7.62mm_Py12.70mm_Pulse_LP-44')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

