
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Disc_D12.0mm_W4.4mm_P7.75mm"
    hexID = "FZKCCDISCD12W44P775"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Disc_D12.0mm_W4.4mm_P7.75mm', 'description': 'C, Disc series, Radial, pin pitch=7.75mm, , diameter*width=12*4.4mm^2, Capacitor', 'tags': 'C Disc series Radial pin pitch 7.75mm  diameter 12mm width 4.4mm Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Disc_D12.0mm_W4.4mm_P7.75mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Disc_D12.0mm_W4.4mm_P7.75mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

