
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Axial_Shunt_L22.2mm_W9.5mm_PS14.30mm_P25.40mm"
    hexID = "FZKRRAXIALSHUNTL222W95PS143P254"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Axial_Shunt_L22.2mm_W9.5mm_PS14.30mm_P25.40mm', 'description': 'Resistor, Axial_Shunt series, Box, pin pitch=25.4mm, 5W, length*width*height=22.2*9.5*9.5mm^3, shunt pin pitch = 14.30mm, http://www.vishay.com/docs/30217/cpsl.pdf', 'tags': 'Resistor Axial_Shunt series Box pin pitch 25.4mm 5W length 22.2mm width 9.5mm height 9.5mm shunt pin pitch 14.30mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_Shunt_L22.2mm_W9.5mm_PS14.30mm_P25.40mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Axial_Shunt_L22.2mm_W9.5mm_PS14.30mm_P25.40mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

