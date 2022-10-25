
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Disc_D9.0mm_W5.0mm_P7.50mm"
    hexID = "FZKCCDISCD9W5P75"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Disc_D9.0mm_W5.0mm_P7.50mm', 'description': 'C, Disc series, Radial, pin pitch=7.50mm, , diameter*width=9*5.0mm^2, Capacitor, http://www.vishay.com/docs/28535/vy2series.pdf', 'tags': 'C Disc series Radial pin pitch 7.50mm  diameter 9mm width 5.0mm Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Disc_D9.0mm_W5.0mm_P7.50mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Disc_D9.0mm_W5.0mm_P7.50mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

