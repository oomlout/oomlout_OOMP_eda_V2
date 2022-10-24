
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Module"
    oIndex = "MonoWireless_TWE-L-WX"
    hexID = "FZKRFMOMONOWIRELESSTWELWX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MonoWireless_TWE-L-WX', 'description': 'https://www.mono-wireless.com/jp/products/TWE-LITE/MW-PDS-TWELITE-JP.pdf', 'tags': 'TWE-L-WX', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/MonoWireless_TWE-L-WX.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'oval'}})
    newPart['name'].append('RF_Module : MonoWireless_TWE-L-WX')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

