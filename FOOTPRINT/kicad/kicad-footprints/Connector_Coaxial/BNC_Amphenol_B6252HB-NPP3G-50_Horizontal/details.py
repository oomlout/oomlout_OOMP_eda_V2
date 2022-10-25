
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Coaxial"
    oIndex = "BNC_Amphenol_B6252HB-NPP3G-50_Horizontal"
    hexID = "FZKCNCOABNCAMPHENOLB6252HBNPP3G5HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BNC_Amphenol_B6252HB-NPP3G-50_Horizontal', 'description': 'http://www.farnell.com/datasheets/612848.pdf', 'tags': 'BNC Amphenol Horizontal', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Coaxial.3dshapes/BNC_Amphenol_B6252HB-NPP3G-50_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Connector_Coaxial : BNC_Amphenol_B6252HB-NPP3G-50_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

