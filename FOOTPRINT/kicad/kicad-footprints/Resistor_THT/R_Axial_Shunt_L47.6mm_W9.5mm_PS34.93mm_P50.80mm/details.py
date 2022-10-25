
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Axial_Shunt_L47.6mm_W9.5mm_PS34.93mm_P50.80mm"
    hexID = "FZKRRAXIALSHUNTL476W95PS3493P58"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Axial_Shunt_L47.6mm_W9.5mm_PS34.93mm_P50.80mm', 'description': 'Resistor, Axial_Shunt series, Box, pin pitch=50.8mm, 10W, length*width*height=47.6*9.5*9.5mm^3, shunt pin pitch = 34.93mm, http://www.vishay.com/docs/30217/cpsl.pdf', 'tags': 'Resistor Axial_Shunt series Box pin pitch 50.8mm 10W length 47.6mm width 9.5mm height 9.5mm shunt pin pitch 34.93mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_Shunt_L47.6mm_W9.5mm_PS34.93mm_P50.80mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Axial_Shunt_L47.6mm_W9.5mm_PS34.93mm_P50.80mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

