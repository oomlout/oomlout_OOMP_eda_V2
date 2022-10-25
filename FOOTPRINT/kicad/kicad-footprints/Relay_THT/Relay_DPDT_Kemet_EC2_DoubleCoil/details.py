
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_DPDT_Kemet_EC2_DoubleCoil"
    hexID = "FZKRELRELAYDPDTKEMETEC2DOUBLECOIL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_DPDT_Kemet_EC2_DoubleCoil', 'description': 'Kemet signal relay, DPDT, double coil latching, https://content.kemet.com/datasheets/KEM_R7002_EC2_EE2.pdf', 'tags': 'Kemet EC2 signal relay DPDT double dual coil latching through hole THT', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_DPDT_Kemet_EC2_DoubleCoil.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Relay_THT : Relay_DPDT_Kemet_EC2_DoubleCoil')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

