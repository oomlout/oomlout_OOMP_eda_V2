
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Radial_Power_L12.0mm_W8.0mm_P5.00mm"
    hexID = "FZKRRRPOWERL12W8P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Radial_Power_L12.0mm_W8.0mm_P5.00mm', 'description': 'Resistor, Radial_Power series, Radial, pin pitch=5.00mm, 3W, length*width=12.0*8.0mm^2, http://www.vishay.com/docs/30218/cpcx.pdf', 'tags': 'Resistor Radial_Power series Radial pin pitch 5.00mm 3W length 12.0mm width 8.0mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Radial_Power_L12.0mm_W8.0mm_P5.00mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Radial_Power_L12.0mm_W8.0mm_P5.00mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

