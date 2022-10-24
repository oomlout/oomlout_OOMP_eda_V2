
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Module"
    oIndex = "HOPERF_RFM9XW_SMD"
    hexID = "FZKRFMOHOPERFRFM9XWSM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HOPERF_RFM9XW_SMD', 'description': 'Low Power Long Range Transceiver Module SMD-16 (https://www.hoperf.com/data/upload/portal/20181127/5bfcbea20e9ef.pdf)', 'tags': 'LoRa Low Power Long Range Transceiver Module', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/HOPERF_RFM9XW_SMD.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Module : HOPERF_RFM9XW_SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

