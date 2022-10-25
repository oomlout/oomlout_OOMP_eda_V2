
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L20.0mm_D8.0mm_P7.62mm_Vertical"
    hexID = "FZKINLAXIALL2D8P762VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L20.0mm_D8.0mm_P7.62mm_Vertical', 'description': 'Inductor, Axial series, Axial, Vertical, pin pitch=7.62mm, , length*diameter=20*8mm^2', 'tags': 'Inductor Axial series Axial Vertical pin pitch 7.62mm  length 20mm diameter 8mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L20.0mm_D8.0mm_P7.62mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L20.0mm_D8.0mm_P7.62mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

