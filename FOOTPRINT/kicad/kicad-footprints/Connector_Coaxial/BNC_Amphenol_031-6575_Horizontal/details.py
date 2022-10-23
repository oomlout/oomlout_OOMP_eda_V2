
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Coaxial"
    oIndex = "BNC_Amphenol_031-6575_Horizontal"
    hexID = "FZKCNCOABNCAMPHENOL316575HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BNC_Amphenol_031-6575_Horizontal', 'description': 'dual independently isolated BNC plug (https://www.amphenolrf.com/downloads/dl/file/id/2980/product/644/031_6575_customer_drawing.pdf)', 'tags': 'Dual BNC Amphenol Horizontal', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Coaxial.3dshapes/BNC_Amphenol_031-6575_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Connector_Coaxial : BNC_Amphenol_031-6575_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

