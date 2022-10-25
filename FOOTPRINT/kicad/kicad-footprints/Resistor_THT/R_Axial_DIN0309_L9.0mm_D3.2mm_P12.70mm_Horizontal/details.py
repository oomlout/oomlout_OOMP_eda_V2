
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal"
    hexID = "FZKRRAXIALDIN39L9D32P127HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal', 'description': 'Resistor, Axial_DIN0309 series, Axial, Horizontal, pin pitch=12.7mm, 0.5W = 1/2W, length*diameter=9*3.2mm^2, http://cdn-reichelt.de/documents/datenblatt/B400/1_4W%23YAG.pdf', 'tags': 'Resistor Axial_DIN0309 series Axial Horizontal pin pitch 12.7mm 0.5W = 1/2W length 9mm diameter 3.2mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

