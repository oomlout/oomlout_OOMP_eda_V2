
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Card"
    oIndex = "microSD_HC_Hirose_DM3D-SF"
    hexID = "FZKCNCARDMSDHCHIROSEDM3DSF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'microSD_HC_Hirose_DM3D-SF', 'description': 'Micro SD, SMD, right-angle, push-pull (https://media.digikey.com/PDF/Data%20Sheets/Hirose%20PDFs/DM3D-SF.pdf)', 'tags': 'Micro SD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Card.3dshapes/microSD_HC_Hirose_DM3D-SF.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Card : microSD_HC_Hirose_DM3D-SF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

