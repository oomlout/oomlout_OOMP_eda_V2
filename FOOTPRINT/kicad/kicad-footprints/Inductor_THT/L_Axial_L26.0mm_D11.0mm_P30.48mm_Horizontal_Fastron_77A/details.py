
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L26.0mm_D11.0mm_P30.48mm_Horizontal_Fastron_77A"
    hexID = "FZKINLAXIALL26D11P348HORIZONTALFASTRON77A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L26.0mm_D11.0mm_P30.48mm_Horizontal_Fastron_77A', 'description': 'Inductor, Axial series, Axial, Horizontal, pin pitch=30.48mm, , length*diameter=26*11mm^2, Fastron, 77A, http://cdn-reichelt.de/documents/datenblatt/B400/DS_77A.pdf', 'tags': 'Inductor Axial series Axial Horizontal pin pitch 30.48mm  length 26mm diameter 11mm Fastron 77A', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L26.0mm_D11.0mm_P30.48mm_Horizontal_Fastron_77A.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L26.0mm_D11.0mm_P30.48mm_Horizontal_Fastron_77A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

