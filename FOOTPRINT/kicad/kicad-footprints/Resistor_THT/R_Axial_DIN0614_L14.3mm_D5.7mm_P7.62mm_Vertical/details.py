
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Axial_DIN0614_L14.3mm_D5.7mm_P7.62mm_Vertical"
    hexID = "FZKRRAXIALDIN614L143D57P762VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Axial_DIN0614_L14.3mm_D5.7mm_P7.62mm_Vertical', 'description': 'Resistor, Axial_DIN0614 series, Axial, Vertical, pin pitch=7.62mm, 1.5W, length*diameter=14.3*5.7mm^2', 'tags': 'Resistor Axial_DIN0614 series Axial Vertical pin pitch 7.62mm 1.5W length 14.3mm diameter 5.7mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_DIN0614_L14.3mm_D5.7mm_P7.62mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Axial_DIN0614_L14.3mm_D5.7mm_P7.62mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

