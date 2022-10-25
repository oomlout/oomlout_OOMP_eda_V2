
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Card"
    oIndex = "microSIM_JAE_SF53S006VCBR2000"
    hexID = "FZKCNCARDMSIMJAESF53S6VCBR2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'microSIM_JAE_SF53S006VCBR2000', 'description': 'https://www.jae.com/z-en/pdf_download_exec.cfm?param=SJ115712.pdf', 'tags': 'microSIM GSM Card', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Card.3dshapes/microSIM_JAE_SF53S006VCBR2000.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Card : microSIM_JAE_SF53S006VCBR2000')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

