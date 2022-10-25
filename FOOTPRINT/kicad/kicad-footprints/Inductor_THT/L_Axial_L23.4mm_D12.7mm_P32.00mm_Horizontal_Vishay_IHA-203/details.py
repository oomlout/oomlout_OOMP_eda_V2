
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L23.4mm_D12.7mm_P32.00mm_Horizontal_Vishay_IHA-203"
    hexID = "FZKINLAXIALL234D127P32HORIZONTALVISHAYIHA23"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L23.4mm_D12.7mm_P32.00mm_Horizontal_Vishay_IHA-203', 'description': 'Inductor, Axial series, Axial, Horizontal, pin pitch=32mm, , length*diameter=23.37*12.7mm^2, Vishay, IHA-203, http://www.vishay.com/docs/34014/iha.pdf', 'tags': 'Inductor Axial series Axial Horizontal pin pitch 32mm  length 23.37mm diameter 12.7mm Vishay IHA-203', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L23.4mm_D12.7mm_P32.00mm_Horizontal_Vishay_IHA-203.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L23.4mm_D12.7mm_P32.00mm_Horizontal_Vishay_IHA-203')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

