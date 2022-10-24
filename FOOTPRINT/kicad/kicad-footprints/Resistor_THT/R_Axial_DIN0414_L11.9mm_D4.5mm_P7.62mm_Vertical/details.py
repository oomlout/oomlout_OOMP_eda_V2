
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Axial_DIN0414_L11.9mm_D4.5mm_P7.62mm_Vertical"
    hexID = "FZKRRAXIALDIN414L119D45P762VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Axial_DIN0414_L11.9mm_D4.5mm_P7.62mm_Vertical', 'description': 'Resistor, Axial_DIN0414 series, Axial, Vertical, pin pitch=7.62mm, 2W, length*diameter=11.9*4.5mm^2, http://www.vishay.com/docs/20128/wkxwrx.pdf', 'tags': 'Resistor Axial_DIN0414 series Axial Vertical pin pitch 7.62mm 2W length 11.9mm diameter 4.5mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_DIN0414_L11.9mm_D4.5mm_P7.62mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Axial_DIN0414_L11.9mm_D4.5mm_P7.62mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

