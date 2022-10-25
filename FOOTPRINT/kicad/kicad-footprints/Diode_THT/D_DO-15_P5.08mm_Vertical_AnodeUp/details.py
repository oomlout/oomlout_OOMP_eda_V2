
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "D_DO-15_P5.08mm_Vertical_AnodeUp"
    hexID = "FZKDDDO15P58VERTICALANODEUP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_DO-15_P5.08mm_Vertical_AnodeUp', 'description': 'Diode, DO-15 series, Axial, Vertical, pin pitch=5.08mm, , length*diameter=7.6*3.6mm^2, , http://www.diodes.com/_files/packages/DO-15.pdf', 'tags': 'Diode DO-15 series Axial Vertical pin pitch 5.08mm  length 7.6mm diameter 3.6mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_DO-15_P5.08mm_Vertical_AnodeUp.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : D_DO-15_P5.08mm_Vertical_AnodeUp')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

