
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L20.3mm_D12.1mm_P28.50mm_Horizontal_Vishay_IHA-101"
    hexID = "FZKINLAXIALL23D121P285HORIZONTALVISHAYIHA11"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L20.3mm_D12.1mm_P28.50mm_Horizontal_Vishay_IHA-101', 'description': 'Inductor, Axial series, Axial, Horizontal, pin pitch=28.5mm, , length*diameter=20.32*12.07mm^2, Vishay, IHA-101, http://www.vishay.com/docs/34014/iha.pdf', 'tags': 'Inductor Axial series Axial Horizontal pin pitch 28.5mm  length 20.32mm diameter 12.07mm Vishay IHA-101', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L20.3mm_D12.1mm_P28.50mm_Horizontal_Vishay_IHA-101.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L20.3mm_D12.1mm_P28.50mm_Horizontal_Vishay_IHA-101')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

