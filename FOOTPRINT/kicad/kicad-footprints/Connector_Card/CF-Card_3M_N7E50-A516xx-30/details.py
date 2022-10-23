
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Card"
    oIndex = "CF-Card_3M_N7E50-A516xx-30"
    hexID = "FZKCNCARDCFCARD3MN7E5A516XX3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CF-Card_3M_N7E50-A516xx-30', 'description': 'Compact Flash Card connector, polarization inverse (https://multimedia.3m.com/mws/media/22424O/3mtm-cf-card-header-type-i-low-profile-surface-mount-ts0747.pdf)', 'tags': 'connector cf', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Card.3dshapes/CF-Card_3M_N7E50-A516xx-30.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Card : CF-Card_3M_N7E50-A516xx-30')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

