
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Disc_D7.5mm_W4.4mm_P5.00mm"
    hexID = "FZKCCDISCD75W44P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Disc_D7.5mm_W4.4mm_P5.00mm', 'description': 'C, Disc series, Radial, pin pitch=5.00mm, , diameter*width=7.5*4.4mm^2, Capacitor', 'tags': 'C Disc series Radial pin pitch 5.00mm  diameter 7.5mm width 4.4mm Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Disc_D7.5mm_W4.4mm_P5.00mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Disc_D7.5mm_W4.4mm_P5.00mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

