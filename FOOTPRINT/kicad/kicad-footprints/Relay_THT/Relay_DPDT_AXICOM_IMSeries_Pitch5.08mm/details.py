
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_DPDT_AXICOM_IMSeries_Pitch5.08mm"
    hexID = "FZKRELRELAYDPDTAXICOMIMSERIESPITCH58"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_DPDT_AXICOM_IMSeries_Pitch5.08mm', 'description': 'AXICOM IM-Series Relays, DPDR, Pitch 5.08', 'tags': 'AXICOM IM-Series Relay DPDR Pitch 5.08', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_DPDT_AXICOM_IMSeries_Pitch5.08mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Relay_THT : Relay_DPDT_AXICOM_IMSeries_Pitch5.08mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

