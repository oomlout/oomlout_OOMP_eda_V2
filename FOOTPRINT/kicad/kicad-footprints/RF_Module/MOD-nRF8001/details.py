
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Module"
    oIndex = "MOD-nRF8001"
    hexID = "FZKRFMOMODNRF81"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MOD-nRF8001', 'description': 'BLE module, https://www.olimex.com/Products/Modules/RF/MOD-nRF8001/', 'tags': 'BLE module', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/MOD-nRF8001.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Module : MOD-nRF8001')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

