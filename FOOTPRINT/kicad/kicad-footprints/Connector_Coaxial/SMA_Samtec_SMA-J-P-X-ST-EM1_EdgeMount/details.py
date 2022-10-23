
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Coaxial"
    oIndex = "SMA_Samtec_SMA-J-P-X-ST-EM1_EdgeMount"
    hexID = "FZKCNCOASSAMTECSJPXSTEM1EDGEMOUNT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SMA_Samtec_SMA-J-P-X-ST-EM1_EdgeMount', 'description': 'Connector SMA, 0Hz to 20GHz, 50Ohm, Edge Mount (http://suddendocs.samtec.com/prints/sma-j-p-x-st-em1-mkt.pdf)', 'tags': 'SMA Straight Samtec Edge Mount', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Coaxial.3dshapes/SMA_Samtec_SMA-J-P-X-ST-EM1_EdgeMount.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Coaxial : SMA_Samtec_SMA-J-P-X-ST-EM1_EdgeMount')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

