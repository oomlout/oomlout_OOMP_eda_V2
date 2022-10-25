
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Axial_L19.0mm_D7.5mm_P25.00mm_Horizontal"
    hexID = "FZKCCAXIALL19D75P25HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Axial_L19.0mm_D7.5mm_P25.00mm_Horizontal', 'description': 'C, Axial series, Axial, Horizontal, pin pitch=25mm, , length*diameter=19*7.5mm^2, http://cdn-reichelt.de/documents/datenblatt/B300/STYROFLEX.pdf', 'tags': 'C Axial series Axial Horizontal pin pitch 25mm  length 19mm diameter 7.5mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Axial_L19.0mm_D7.5mm_P25.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Axial_L19.0mm_D7.5mm_P25.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

