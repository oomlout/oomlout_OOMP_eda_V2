
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L26.0mm_D10.0mm_P7.62mm_Vertical_Fastron_77A"
    hexID = "FZKINLAXIALL26D1P762VERTICALFASTRON77A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L26.0mm_D10.0mm_P7.62mm_Vertical_Fastron_77A', 'description': 'Inductor, Axial series, Axial, Vertical, pin pitch=7.62mm, , length*diameter=26*10mm^2, Fastron, 77A, http://cdn-reichelt.de/documents/datenblatt/B400/DS_77A.pdf', 'tags': 'Inductor Axial series Axial Vertical pin pitch 7.62mm  length 26mm diameter 10mm Fastron 77A', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L26.0mm_D10.0mm_P7.62mm_Vertical_Fastron_77A.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L26.0mm_D10.0mm_P7.62mm_Vertical_Fastron_77A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

