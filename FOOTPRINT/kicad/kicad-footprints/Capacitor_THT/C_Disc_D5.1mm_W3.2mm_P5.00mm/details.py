
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Disc_D5.1mm_W3.2mm_P5.00mm"
    hexID = "FZKCCDISCD51W32P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Disc_D5.1mm_W3.2mm_P5.00mm', 'description': 'C, Disc series, Radial, pin pitch=5.00mm, , diameter*width=5.1*3.2mm^2, Capacitor, http://www.vishay.com/docs/45233/krseries.pdf', 'tags': 'C Disc series Radial pin pitch 5.00mm  diameter 5.1mm width 3.2mm Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Disc_D5.1mm_W3.2mm_P5.00mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Disc_D5.1mm_W3.2mm_P5.00mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

