
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Amphenol"
    oIndex = "Amphenol_M8S-03PMMR-SF8001"
    hexID = "FZKCNAMPHENOLAMPHENOLM8S3PRSF81"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Amphenol_M8S-03PMMR-SF8001', 'description': 'M8 Male connector for panel, 90° PCB mount (https://www.amphenolltw.com/2012download/2D%20PDF/03_M%20Series%20Sensor%20Connectors/M8S-XXPMMR-SF8001.pdf)', 'tags': 'three-pin M8', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Amphenol.3dshapes/Amphenol_M8S-03PMMR-SF8001.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_Amphenol : Amphenol_M8S-03PMMR-SF8001')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

