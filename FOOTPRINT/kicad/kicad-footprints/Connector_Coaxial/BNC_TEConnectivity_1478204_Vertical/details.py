
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Coaxial"
    oIndex = "BNC_TEConnectivity_1478204_Vertical"
    hexID = "FZKCNCOABNCTECONNECTIVITY147824VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BNC_TEConnectivity_1478204_Vertical', 'description': 'BNC female PCB mount 4 pin straight chassis connector http://www.te.com/usa-en/product-1-1478204-0.html', 'tags': 'BNC female PCB mount 4 pin straight chassis connector ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Coaxial.3dshapes/BNC_TEConnectivity_1478204_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Coaxial : BNC_TEConnectivity_1478204_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

