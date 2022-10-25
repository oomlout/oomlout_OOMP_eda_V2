
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L6.6mm_D2.7mm_P2.54mm_Vertical_Vishay_IM-2"
    hexID = "FZKINLAXIALL66D27P254VERTICALVISHAYIM2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L6.6mm_D2.7mm_P2.54mm_Vertical_Vishay_IM-2', 'description': 'Inductor, Axial series, Axial, Vertical, pin pitch=2.54mm, , length*diameter=6.6*2.7mm^2, Vishay, IM-2, http://www.vishay.com/docs/34030/im.pdf', 'tags': 'Inductor Axial series Axial Vertical pin pitch 2.54mm  length 6.6mm diameter 2.7mm Vishay IM-2', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L6.6mm_D2.7mm_P2.54mm_Vertical_Vishay_IM-2.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L6.6mm_D2.7mm_P2.54mm_Vertical_Vishay_IM-2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

