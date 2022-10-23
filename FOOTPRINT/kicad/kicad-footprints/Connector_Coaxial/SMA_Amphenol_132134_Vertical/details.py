
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Coaxial"
    oIndex = "SMA_Amphenol_132134_Vertical"
    hexID = "FZKCNCOASAMPHENOL132134VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SMA_Amphenol_132134_Vertical', 'description': 'https://www.amphenolrf.com/downloads/dl/file/id/2187/product/2843/132134_customer_drawing.pdf', 'tags': 'SMA THT Female Jack Vertical ExtendedLegs', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Coaxial.3dshapes/SMA_Amphenol_132134_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Coaxial : SMA_Amphenol_132134_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

