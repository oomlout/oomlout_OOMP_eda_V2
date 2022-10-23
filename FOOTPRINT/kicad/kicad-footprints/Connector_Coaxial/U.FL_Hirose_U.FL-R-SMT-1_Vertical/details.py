
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Coaxial"
    oIndex = "U.FL_Hirose_U.FL-R-SMT-1_Vertical"
    hexID = "FZKCNCOAUFLHIROSEUFLRS1VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'U.FL_Hirose_U.FL-R-SMT-1_Vertical', 'description': 'Hirose U.FL Coaxial https://www.hirose.com/product/en/products/U.FL/U.FL-R-SMT-1%2810%29/', 'tags': 'Hirose U.FL Coaxial', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Coaxial.3dshapes/U.FL_Hirose_U.FL-R-SMT-1_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Coaxial : U.FL_Hirose_U.FL-R-SMT-1_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

