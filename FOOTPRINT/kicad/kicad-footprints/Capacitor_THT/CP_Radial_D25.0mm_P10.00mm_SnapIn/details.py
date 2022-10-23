
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "CP_Radial_D25.0mm_P10.00mm_SnapIn"
    hexID = "FZKCCPRD25P1SNAPIN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CP_Radial_D25.0mm_P10.00mm_SnapIn', 'description': 'CP, Radial series, Radial, pin pitch=10.00mm, , diameter=25mm, Electrolytic Capacitor, , http://www.vishay.com/docs/28342/058059pll-si.pdf', 'tags': 'CP Radial series Radial pin pitch 10.00mm  diameter 25mm Electrolytic Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/CP_Radial_D25.0mm_P10.00mm_SnapIn.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Capacitor_THT : CP_Radial_D25.0mm_P10.00mm_SnapIn')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

