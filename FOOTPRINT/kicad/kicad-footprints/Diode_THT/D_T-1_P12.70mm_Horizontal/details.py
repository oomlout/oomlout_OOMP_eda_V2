
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "D_T-1_P12.70mm_Horizontal"
    hexID = "FZKDDT1P127HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_T-1_P12.70mm_Horizontal', 'description': 'Diode, T-1 series, Axial, Horizontal, pin pitch=12.7mm, , length*diameter=3.2*2.6mm^2, , http://www.diodes.com/_files/packages/T-1.pdf', 'tags': 'Diode T-1 series Axial Horizontal pin pitch 12.7mm  length 3.2mm diameter 2.6mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_T-1_P12.70mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : D_T-1_P12.70mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

