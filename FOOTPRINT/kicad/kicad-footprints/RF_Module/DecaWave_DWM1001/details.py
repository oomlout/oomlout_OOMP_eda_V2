
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Module"
    oIndex = "DecaWave_DWM1001"
    hexID = "FZKRFMODECAWAVEDWM11"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DecaWave_DWM1001', 'description': 'https://www.decawave.com/sites/default/files/dwm1001_datasheet.pdf', 'tags': 'UWB module', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/DecaWave_DWM1001.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('RF_Module : DecaWave_DWM1001')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

