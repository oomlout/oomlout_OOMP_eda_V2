
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "D_DO-201_P15.24mm_Horizontal"
    hexID = "FZKDDDO21P1524HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_DO-201_P15.24mm_Horizontal', 'description': 'Diode, DO-201 series, Axial, Horizontal, pin pitch=15.24mm, , length*diameter=9.53*5.21mm^2, , http://www.diodes.com/_files/packages/DO-201.pdf', 'tags': 'Diode DO-201 series Axial Horizontal pin pitch 15.24mm  length 9.53mm diameter 5.21mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_DO-201_P15.24mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : D_DO-201_P15.24mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

