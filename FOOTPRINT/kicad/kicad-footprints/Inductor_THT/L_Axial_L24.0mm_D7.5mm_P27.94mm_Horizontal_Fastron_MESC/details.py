
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L24.0mm_D7.5mm_P27.94mm_Horizontal_Fastron_MESC"
    hexID = "FZKINLAXIALL24D75P2794HORIZONTALFASTRONMESC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L24.0mm_D7.5mm_P27.94mm_Horizontal_Fastron_MESC', 'description': 'Inductor, Axial series, Axial, Horizontal, pin pitch=27.94mm, , length*diameter=24*7.5mm^2, Fastron, MESC, http://cdn-reichelt.de/documents/datenblatt/B400/DS_MESC.pdf', 'tags': 'Inductor Axial series Axial Horizontal pin pitch 27.94mm  length 24mm diameter 7.5mm Fastron MESC', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L24.0mm_D7.5mm_P27.94mm_Horizontal_Fastron_MESC.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L24.0mm_D7.5mm_P27.94mm_Horizontal_Fastron_MESC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

