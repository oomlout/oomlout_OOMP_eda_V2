
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "CP_Axial_L38.0mm_D21.0mm_P44.00mm_Horizontal"
    hexID = "FZKCCPAXIALL38D21P44HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CP_Axial_L38.0mm_D21.0mm_P44.00mm_Horizontal', 'description': 'CP, Axial series, Axial, Horizontal, pin pitch=44mm, , length*diameter=38*21mm^2, Electrolytic Capacitor, , http://www.vishay.com/docs/28325/021asm.pdf', 'tags': 'CP Axial series Axial Horizontal pin pitch 44mm  length 38mm diameter 21mm Electrolytic Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/CP_Axial_L38.0mm_D21.0mm_P44.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Capacitor_THT : CP_Axial_L38.0mm_D21.0mm_P44.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

