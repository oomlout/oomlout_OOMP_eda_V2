
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_SMD"
    oIndex = "CP_Elec_10x14.3"
    hexID = "FZKCAPACITORSMCPELEC1X143"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CP_Elec_10x14.3', 'description': 'SMD capacitor, aluminum electrolytic, Vishay 1014, 10.0x14.3mm, http://www.vishay.com/docs/28395/150crz.pdf', 'tags': 'capacitor electrolytic', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_SMD.3dshapes/CP_Elec_10x14.3.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Capacitor_SMD : CP_Elec_10x14.3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

