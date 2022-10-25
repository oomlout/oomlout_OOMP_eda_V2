
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "D_DO-201AE_P3.81mm_Vertical_AnodeUp"
    hexID = "FZKDDDO21AEP381VERTICALANODEUP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_DO-201AE_P3.81mm_Vertical_AnodeUp', 'description': 'Diode, DO-201AE series, Axial, Vertical, pin pitch=3.81mm, , length*diameter=9*5.3mm^2, , http://www.farnell.com/datasheets/529758.pdf', 'tags': 'Diode DO-201AE series Axial Vertical pin pitch 3.81mm  length 9mm diameter 5.3mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_DO-201AE_P3.81mm_Vertical_AnodeUp.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : D_DO-201AE_P3.81mm_Vertical_AnodeUp')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

