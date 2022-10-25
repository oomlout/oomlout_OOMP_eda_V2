
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "D_5W_P5.08mm_Vertical_KathodeUp"
    hexID = "FZKDD5WP58VERTICALKATHODEUP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_5W_P5.08mm_Vertical_KathodeUp', 'description': 'Diode, 5W series, Axial, Vertical, pin pitch=5.08mm, , length*diameter=8.9*3.7mm^2, , http://www.diodes.com/_files/packages/8686949.gif', 'tags': 'Diode 5W series Axial Vertical pin pitch 5.08mm  length 8.9mm diameter 3.7mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_5W_P5.08mm_Vertical_KathodeUp.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : D_5W_P5.08mm_Vertical_KathodeUp')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

