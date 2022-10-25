
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Bare_Metal_Element_L21.3mm_W4.8mm_P20.30mm"
    hexID = "FZKRRBAREMETALELEMENTL213W48P23"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Bare_Metal_Element_L21.3mm_W4.8mm_P20.30mm', 'description': 'Resistor, Bare_Metal_Element series, Bare Metal Strip/Wire, Horizontal, pin pitch=20.3mm, 5W, length*width=21.3*4.8mm^2, https://www.bourns.com/pdfs/PWR4412-2S.pdf', 'tags': 'Resistor Bare_Metal_Element series Bare Metal Strip Wire Horizontal pin pitch 20.3mm 5W length 21.3mm width 4.8mm ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Bare_Metal_Element_L21.3mm_W4.8mm_P20.30mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Bare_Metal_Element_L21.3mm_W4.8mm_P20.30mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

