
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_SPDT_PotterBrumfield_T9AP5D52_12V30A"
    hexID = "FZKRELRELAYSPDTPOTTERBRUMFIELDT9AP5D5212V3A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_SPDT_PotterBrumfield_T9AP5D52_12V30A', 'description': 'Relay SPDT Potter&Brumfield T9AP5D52 12V 30A 1xUn Connector Fast ON Only Dummy for Space NO Pads', 'tags': 'Relay SPDT Potter&Brumfield T9AP5D52 12V 30A 1xUm Connector Fast ON Flachsteckeranschluss Only Dummy for Space NO Pads', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_SPDT_PotterBrumfield_T9AP5D52_12V30A.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Relay_THT : Relay_SPDT_PotterBrumfield_T9AP5D52_12V30A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

