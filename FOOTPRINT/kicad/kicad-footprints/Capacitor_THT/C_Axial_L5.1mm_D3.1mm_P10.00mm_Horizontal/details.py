
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Axial_L5.1mm_D3.1mm_P10.00mm_Horizontal"
    hexID = "FZKCCAXIALL51D31P1HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Axial_L5.1mm_D3.1mm_P10.00mm_Horizontal', 'description': 'C, Axial series, Axial, Horizontal, pin pitch=10mm, , length*diameter=5.1*3.1mm^2, http://www.vishay.com/docs/45231/arseries.pdf', 'tags': 'C Axial series Axial Horizontal pin pitch 10mm  length 5.1mm diameter 3.1mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Axial_L5.1mm_D3.1mm_P10.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Axial_L5.1mm_D3.1mm_P10.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

