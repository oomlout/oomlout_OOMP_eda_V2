
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L24.0mm_D7.1mm_P30.48mm_Horizontal_Vishay_IM-10-28"
    hexID = "FZKINLAXIALL24D71P348HORIZONTALVISHAYIM128"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L24.0mm_D7.1mm_P30.48mm_Horizontal_Vishay_IM-10-28', 'description': 'Inductor, Axial series, Axial, Horizontal, pin pitch=30.48mm, , length*diameter=24*7.1mm^2, Vishay, IM-10-28, http://www.vishay.com/docs/34035/im10.pdf', 'tags': 'Inductor Axial series Axial Horizontal pin pitch 30.48mm  length 24mm diameter 7.1mm Vishay IM-10-28', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L24.0mm_D7.1mm_P30.48mm_Horizontal_Vishay_IM-10-28.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L24.0mm_D7.1mm_P30.48mm_Horizontal_Vishay_IM-10-28')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

