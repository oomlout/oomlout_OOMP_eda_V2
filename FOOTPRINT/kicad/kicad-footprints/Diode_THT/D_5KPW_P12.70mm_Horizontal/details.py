
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "D_5KPW_P12.70mm_Horizontal"
    hexID = "FZKDD5KPWP127HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_5KPW_P12.70mm_Horizontal', 'description': 'Diode, 5KPW series, Axial, Horizontal, pin pitch=12.7mm, , length*diameter=9*8mm^2, , http://www.diodes.com/_files/packages/8686949.gif', 'tags': 'Diode 5KPW series Axial Horizontal pin pitch 12.7mm  length 9mm diameter 8mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_5KPW_P12.70mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : D_5KPW_P12.70mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

