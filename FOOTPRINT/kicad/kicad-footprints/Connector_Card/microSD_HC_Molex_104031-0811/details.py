
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Card"
    oIndex = "microSD_HC_Molex_104031-0811"
    hexID = "FZKCNCARDMSDHCMX1431811"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'microSD_HC_Molex_104031-0811', 'description': '1.10mm Pitch microSD Memory Card Connector, Surface Mount, Push-Pull Type, 1.42mm Height, with Detect Switch (https://www.molex.com/pdm_docs/sd/1040310811_sd.pdf)', 'tags': 'microSD SD molex', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Card.3dshapes/microSD_HC_Molex_104031-0811.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Card : microSD_HC_Molex_104031-0811')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

