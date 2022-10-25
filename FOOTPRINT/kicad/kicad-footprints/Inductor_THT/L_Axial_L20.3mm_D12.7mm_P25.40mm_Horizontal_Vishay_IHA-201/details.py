
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L20.3mm_D12.7mm_P25.40mm_Horizontal_Vishay_IHA-201"
    hexID = "FZKINLAXIALL23D127P254HORIZONTALVISHAYIHA21"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L20.3mm_D12.7mm_P25.40mm_Horizontal_Vishay_IHA-201', 'description': 'Inductor, Axial series, Axial, Horizontal, pin pitch=25.4mm, , length*diameter=20.32*12.7mm^2, Vishay, IHA-201, http://www.vishay.com/docs/34014/iha.pdf', 'tags': 'Inductor Axial series Axial Horizontal pin pitch 25.4mm  length 20.32mm diameter 12.7mm Vishay IHA-201', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L20.3mm_D12.7mm_P25.40mm_Horizontal_Vishay_IHA-201.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L20.3mm_D12.7mm_P25.40mm_Horizontal_Vishay_IHA-201')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

