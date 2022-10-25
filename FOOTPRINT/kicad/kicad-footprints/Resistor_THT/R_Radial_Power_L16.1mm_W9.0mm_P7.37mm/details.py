
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Radial_Power_L16.1mm_W9.0mm_P7.37mm"
    hexID = "FZKRRRPOWERL161W9P737"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Radial_Power_L16.1mm_W9.0mm_P7.37mm', 'description': 'Resistor, Radial_Power series, Radial, pin pitch=7.37mm, 10W, length*width=16.1*9mm^2, http://www.vishay.com/docs/30218/cpcx.pdf', 'tags': 'Resistor Radial_Power series Radial pin pitch 7.37mm 10W length 16.1mm width 9mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Radial_Power_L16.1mm_W9.0mm_P7.37mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Radial_Power_L16.1mm_W9.0mm_P7.37mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

