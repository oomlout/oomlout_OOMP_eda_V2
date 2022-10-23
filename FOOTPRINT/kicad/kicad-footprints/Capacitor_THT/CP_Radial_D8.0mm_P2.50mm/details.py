
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "CP_Radial_D8.0mm_P2.50mm"
    hexID = "FZKCCPRD8P25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CP_Radial_D8.0mm_P2.50mm', 'description': 'CP, Radial series, Radial, pin pitch=2.50mm, , diameter=8mm, Electrolytic Capacitor', 'tags': 'CP Radial series Radial pin pitch 2.50mm  diameter 8mm Electrolytic Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/CP_Radial_D8.0mm_P2.50mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Capacitor_THT : CP_Radial_D8.0mm_P2.50mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

