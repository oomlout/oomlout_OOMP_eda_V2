
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "D_A-405_P12.70mm_Horizontal"
    hexID = "FZKDDA45P127HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_A-405_P12.70mm_Horizontal', 'description': 'Diode, A-405 series, Axial, Horizontal, pin pitch=12.7mm, , length*diameter=5.2*2.7mm^2, , http://www.diodes.com/_files/packages/A-405.pdf', 'tags': 'Diode A-405 series Axial Horizontal pin pitch 12.7mm  length 5.2mm diameter 2.7mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_A-405_P12.70mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : D_A-405_P12.70mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

