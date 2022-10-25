
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JAE"
    oIndex = "JAE_SIM_Card_SF72S006"
    hexID = "FZKCNJAEJAESIMCARDSF72S6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JAE_SIM_Card_SF72S006', 'description': 'SIM Card, Push-Push, https://www.jae.com/direct/topics/topics_file_download/topics_id=68892&ext_no=06&index=0&_lang=en&v=202003111511468456809', 'tags': 'SIM Card with Detect Switch', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JAE.3dshapes/JAE_SIM_Card_SF72S006.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_JAE : JAE_SIM_Card_SF72S006')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

