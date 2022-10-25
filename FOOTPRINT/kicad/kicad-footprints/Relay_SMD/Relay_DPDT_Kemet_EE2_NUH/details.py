
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_SMD"
    oIndex = "Relay_DPDT_Kemet_EE2_NUH"
    hexID = "FZKRELAYSMRELAYDPDTKEMETEE2NUH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_DPDT_Kemet_EE2_NUH', 'description': 'Kemet signal relay, DPDT, double coil latching, https://content.kemet.com/datasheets/KEM_R7002_EC2_EE2.pdf', 'tags': 'Kemet EC2 signal relay DPDT double coil latching surface mount SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_SMD.3dshapes/Relay_DPDT_Kemet_EE2_NUH.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Relay_SMD : Relay_DPDT_Kemet_EE2_NUH')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

