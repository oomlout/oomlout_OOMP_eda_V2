
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Rect_L4.6mm_W4.6mm_P2.50mm_MKS02_FKP02"
    hexID = "FZKCCRECTL46W46P25MKS2FKP2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Rect_L4.6mm_W4.6mm_P2.50mm_MKS02_FKP02', 'description': 'C, Rect series, Radial, pin pitch=2.50mm, , length*width=4.6*4.6mm^2, Capacitor, http://www.wima.de/DE/WIMA_MKS_02.pdf', 'tags': 'C Rect series Radial pin pitch 2.50mm  length 4.6mm width 4.6mm Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Rect_L4.6mm_W4.6mm_P2.50mm_MKS02_FKP02.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Rect_L4.6mm_W4.6mm_P2.50mm_MKS02_FKP02')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

