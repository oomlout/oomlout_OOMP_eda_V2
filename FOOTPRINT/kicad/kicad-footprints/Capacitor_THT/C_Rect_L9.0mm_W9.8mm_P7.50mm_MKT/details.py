
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Rect_L9.0mm_W9.8mm_P7.50mm_MKT"
    hexID = "FZKCCRECTL9W98P75MKT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Rect_L9.0mm_W9.8mm_P7.50mm_MKT', 'description': 'C, Rect series, Radial, pin pitch=7.50mm, , length*width=9*9.8mm^2, Capacitor, https://en.tdk.eu/inf/20/20/db/fc_2009/MKT_B32560_564.pdf', 'tags': 'C Rect series Radial pin pitch 7.50mm  length 9mm width 9.8mm Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Rect_L9.0mm_W9.8mm_P7.50mm_MKT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Rect_L9.0mm_W9.8mm_P7.50mm_MKT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

