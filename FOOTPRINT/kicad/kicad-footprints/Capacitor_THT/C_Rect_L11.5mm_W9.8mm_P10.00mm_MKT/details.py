
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Rect_L11.5mm_W9.8mm_P10.00mm_MKT"
    hexID = "FZKCCRECTL115W98P1MKT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Rect_L11.5mm_W9.8mm_P10.00mm_MKT', 'description': 'C, Rect series, Radial, pin pitch=10.00mm, , length*width=11.5*9.8mm^2, Capacitor, https://en.tdk.eu/inf/20/20/db/fc_2009/MKT_B32560_564.pdf', 'tags': 'C Rect series Radial pin pitch 10.00mm  length 11.5mm width 9.8mm Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Rect_L11.5mm_W9.8mm_P10.00mm_MKT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Rect_L11.5mm_W9.8mm_P10.00mm_MKT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

