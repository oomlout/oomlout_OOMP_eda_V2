
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Axial_DIN0309_L9.0mm_D3.2mm_P5.08mm_Vertical"
    hexID = "FZKRRAXIALDIN39L9D32P58VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Axial_DIN0309_L9.0mm_D3.2mm_P5.08mm_Vertical', 'description': 'Resistor, Axial_DIN0309 series, Axial, Vertical, pin pitch=5.08mm, 0.5W = 1/2W, length*diameter=9*3.2mm^2, http://cdn-reichelt.de/documents/datenblatt/B400/1_4W%23YAG.pdf', 'tags': 'Resistor Axial_DIN0309 series Axial Vertical pin pitch 5.08mm 0.5W = 1/2W length 9mm diameter 3.2mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_DIN0309_L9.0mm_D3.2mm_P5.08mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Axial_DIN0309_L9.0mm_D3.2mm_P5.08mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

