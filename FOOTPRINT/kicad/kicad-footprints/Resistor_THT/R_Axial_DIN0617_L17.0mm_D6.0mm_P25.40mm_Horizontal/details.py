
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Axial_DIN0617_L17.0mm_D6.0mm_P25.40mm_Horizontal"
    hexID = "FZKRRAXIALDIN617L17D6P254HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Axial_DIN0617_L17.0mm_D6.0mm_P25.40mm_Horizontal', 'description': 'Resistor, Axial_DIN0617 series, Axial, Horizontal, pin pitch=25.4mm, 2W, length*diameter=17*6mm^2, http://www.vishay.com/docs/20128/wkxwrx.pdf', 'tags': 'Resistor Axial_DIN0617 series Axial Horizontal pin pitch 25.4mm 2W length 17mm diameter 6mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_DIN0617_L17.0mm_D6.0mm_P25.40mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Axial_DIN0617_L17.0mm_D6.0mm_P25.40mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

