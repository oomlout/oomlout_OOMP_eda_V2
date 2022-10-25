
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "CP_Axial_L55.0mm_D29.0mm_P60.00mm_Horizontal"
    hexID = "FZKCCPAXIALL55D29P6HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CP_Axial_L55.0mm_D29.0mm_P60.00mm_Horizontal', 'description': 'CP, Axial series, Axial, Horizontal, pin pitch=60mm, , length*diameter=55*29.0mm^2, Electrolytic Capacitor, , http://www.vishay.com/docs/42037/53d.pdf', 'tags': 'CP Axial series Axial Horizontal pin pitch 60mm  length 55mm diameter 29.0mm Electrolytic Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/CP_Axial_L55.0mm_D29.0mm_P60.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Capacitor_THT : CP_Axial_L55.0mm_D29.0mm_P60.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

