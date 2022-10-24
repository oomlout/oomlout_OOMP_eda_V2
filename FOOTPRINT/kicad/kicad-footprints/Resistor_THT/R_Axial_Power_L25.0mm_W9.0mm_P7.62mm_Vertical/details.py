
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Axial_Power_L25.0mm_W9.0mm_P7.62mm_Vertical"
    hexID = "FZKRRAXIALPOWERL25W9P762VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Axial_Power_L25.0mm_W9.0mm_P7.62mm_Vertical', 'description': 'Resistor, Axial_Power series, Axial, Vertical, pin pitch=7.62mm, 7W, length*width*height=25*9*9mm^3, http://cdn-reichelt.de/documents/datenblatt/B400/5WAXIAL_9WAXIAL_11WAXIAL_17WAXIAL%23YAG.pdf', 'tags': 'Resistor Axial_Power series Axial Vertical pin pitch 7.62mm 7W length 25mm width 9mm height 9mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_Power_L25.0mm_W9.0mm_P7.62mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Axial_Power_L25.0mm_W9.0mm_P7.62mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

