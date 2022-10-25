
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "D_P600_R-6_P12.70mm_Horizontal"
    hexID = "FZKDDP6R6P127HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_P600_R-6_P12.70mm_Horizontal', 'description': 'Diode, P600_R-6 series, Axial, Horizontal, pin pitch=12.7mm, , length*diameter=9.1*9.1mm^2, , http://www.vishay.com/docs/88692/p600a.pdf, http://www.diodes.com/_files/packages/R-6.pdf', 'tags': 'Diode P600_R-6 series Axial Horizontal pin pitch 12.7mm  length 9.1mm diameter 9.1mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_P600_R-6_P12.70mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : D_P600_R-6_P12.70mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

