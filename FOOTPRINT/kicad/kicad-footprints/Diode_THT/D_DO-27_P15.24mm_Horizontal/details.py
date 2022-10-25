
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "D_DO-27_P15.24mm_Horizontal"
    hexID = "FZKDDDO27P1524HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_DO-27_P15.24mm_Horizontal', 'description': 'Diode, DO-27 series, Axial, Horizontal, pin pitch=15.24mm, , length*diameter=9.52*5.33mm^2, , http://www.slottechforum.com/slotinfo/Techstuff/CD2%20Diodes%20and%20Transistors/Cases/Diode%20DO-27.jpg', 'tags': 'Diode DO-27 series Axial Horizontal pin pitch 15.24mm  length 9.52mm diameter 5.33mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_DO-27_P15.24mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : D_DO-27_P15.24mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

