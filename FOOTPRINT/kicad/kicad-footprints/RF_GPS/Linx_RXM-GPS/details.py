
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_GPS"
    oIndex = "Linx_RXM-GPS"
    hexID = "FZKGPSLINXRXMGPS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Linx_RXM-GPS', 'description': 'GPS Module, Linx (https://linxtechnologies.com/wp/wp-content/uploads/rxm-gps-rm.pdf)', 'tags': 'gps linx', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_GPS.3dshapes/Linx_RXM-GPS.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_GPS : Linx_RXM-GPS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

