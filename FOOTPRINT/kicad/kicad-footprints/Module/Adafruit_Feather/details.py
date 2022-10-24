
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Module"
    oIndex = "Adafruit_Feather"
    hexID = "FZKMOADAFEATHER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Adafruit_Feather', 'description': 'Common footprint for the Adafruit Feather series of boards, https://learn.adafruit.com/adafruit-feather/feather-specification', 'tags': 'Adafruit Feather', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Module.3dshapes/Adafruit_Feather.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Module : Adafruit_Feather')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

