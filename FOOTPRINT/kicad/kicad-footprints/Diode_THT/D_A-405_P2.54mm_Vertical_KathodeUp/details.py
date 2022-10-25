
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "D_A-405_P2.54mm_Vertical_KathodeUp"
    hexID = "FZKDDA45P254VERTICALKATHODEUP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_A-405_P2.54mm_Vertical_KathodeUp', 'description': 'Diode, A-405 series, Axial, Vertical, pin pitch=2.54mm, , length*diameter=5.2*2.7mm^2, , http://www.diodes.com/_files/packages/A-405.pdf', 'tags': 'Diode A-405 series Axial Vertical pin pitch 2.54mm  length 5.2mm diameter 2.7mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_A-405_P2.54mm_Vertical_KathodeUp.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : D_A-405_P2.54mm_Vertical_KathodeUp')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

