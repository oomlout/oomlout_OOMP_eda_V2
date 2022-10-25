
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "CP_Axial_L93.0mm_D23.0mm_P100.00mm_Horizontal"
    hexID = "FZKCCPAXIALL93D23P1HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CP_Axial_L93.0mm_D23.0mm_P100.00mm_Horizontal', 'description': 'CP, Axial series, Axial, Horizontal, pin pitch=100mm, , length*diameter=93*23.0mm^2, Electrolytic Capacitor, , http://www.vishay.com/docs/42037/53d.pdf', 'tags': 'CP Axial series Axial Horizontal pin pitch 100mm  length 93mm diameter 23.0mm Electrolytic Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/CP_Axial_L93.0mm_D23.0mm_P100.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Capacitor_THT : CP_Axial_L93.0mm_D23.0mm_P100.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

