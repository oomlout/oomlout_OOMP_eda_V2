
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Disc_D3.4mm_W2.1mm_P2.50mm"
    hexID = "FZKCCDISCD34W21P25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Disc_D3.4mm_W2.1mm_P2.50mm', 'description': 'C, Disc series, Radial, pin pitch=2.50mm, , diameter*width=3.4*2.1mm^2, Capacitor, http://www.vishay.com/docs/45233/krseries.pdf', 'tags': 'C Disc series Radial pin pitch 2.50mm  diameter 3.4mm width 2.1mm Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Disc_D3.4mm_W2.1mm_P2.50mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Disc_D3.4mm_W2.1mm_P2.50mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

