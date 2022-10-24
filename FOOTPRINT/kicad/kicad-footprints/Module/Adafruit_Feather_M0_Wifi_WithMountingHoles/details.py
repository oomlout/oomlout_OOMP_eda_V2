
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Module"
    oIndex = "Adafruit_Feather_M0_Wifi_WithMountingHoles"
    hexID = "FZKMOADAFEATHERMWIFIWITOUNTINGH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Adafruit_Feather_M0_Wifi_WithMountingHoles', 'description': 'Footprint for the Adafruit Feather M0 Wifi board, https://learn.adafruit.com/adafruit-feather-m0-wifi-atwinc1500/', 'tags': 'Adafruit Feather M0 Wifi', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Module.3dshapes/Adafruit_Feather_M0_Wifi.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Module : Adafruit_Feather_M0_Wifi_WithMountingHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

