
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Axial_DIN0918_L18.0mm_D9.0mm_P7.62mm_Vertical"
    hexID = "FZKRRAXIALDIN918L18D9P762VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Axial_DIN0918_L18.0mm_D9.0mm_P7.62mm_Vertical', 'description': 'Resistor, Axial_DIN0918 series, Axial, Vertical, pin pitch=7.62mm, 4W, length*diameter=18*9mm^2', 'tags': 'Resistor Axial_DIN0918 series Axial Vertical pin pitch 7.62mm 4W length 18mm diameter 9mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_DIN0918_L18.0mm_D9.0mm_P7.62mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Axial_DIN0918_L18.0mm_D9.0mm_P7.62mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

