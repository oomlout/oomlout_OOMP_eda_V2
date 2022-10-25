
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector"
    oIndex = "JWT_A3963_1x02_P3.96mm_Vertical"
    hexID = "FZKCNJWTA39631X2P396VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JWT_A3963_1x02_P3.96mm_Vertical', 'description': 'JWT A3963, 3.96mm pitch Pin head connector (http://www.jwt.com.tw/pro_pdf/A3963.pdf)', 'tags': 'connector JWT A3963 pinhead', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector.3dshapes/JWT_A3963_1x02_P3.96mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector : JWT_A3963_1x02_P3.96mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

