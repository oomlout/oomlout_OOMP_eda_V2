
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Module"
    oIndex = "Raytac_MDBT50Q"
    hexID = "FZKRFMORAYTACMDBT5Q"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Raytac_MDBT50Q', 'description': 'Multiprotocol radio SoC module https://www.raytac.com/download/index.php?index_id=43', 'tags': 'wireless 2.4 GHz Bluetooth ble zigbee 802.15.4 thread nordic raytac nrf52840 nrf52833', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/Raytac_MDBT50Q.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Module : Raytac_MDBT50Q')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

