
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Card"
    oIndex = "microSD_HC_Molex_47219-2001"
    hexID = "FZKCNCARDMSDHCMX4721921"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'microSD_HC_Molex_47219-2001', 'description': '1.10mm Pitch microSD Card Connector, Hinge Type, https://www.molex.com/pdm_docs/sd/472192001_sd.pdf', 'tags': 'Micro SD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Card.3dshapes/microSD_HC_Molex_47219-2001.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Card : microSD_HC_Molex_47219-2001')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

