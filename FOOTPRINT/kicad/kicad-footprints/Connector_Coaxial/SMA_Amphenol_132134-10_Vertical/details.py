
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Coaxial"
    oIndex = "SMA_Amphenol_132134-10_Vertical"
    hexID = "FZKCNCOASAMPHENOL1321341VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SMA_Amphenol_132134-10_Vertical', 'description': 'https://www.amphenolrf.com/downloads/dl/file/id/4007/product/2974/132134_10_customer_drawing.pdf', 'tags': 'SMA SMD Female Jack Vertical', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Coaxial.3dshapes/SMA_Amphenol_132134-10_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Connector_Coaxial : SMA_Amphenol_132134-10_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

