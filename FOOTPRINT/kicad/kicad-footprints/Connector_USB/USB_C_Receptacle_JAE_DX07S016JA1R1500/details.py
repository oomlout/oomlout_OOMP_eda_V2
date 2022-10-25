
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_C_Receptacle_JAE_DX07S016JA1R1500"
    hexID = "FZKCNUUCRECEPTACLEJAEDX7S16JA1R15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_C_Receptacle_JAE_DX07S016JA1R1500', 'description': 'USB TYPE C, USB 2.0, SMT, https://www.jae.com/en/connectors/series/detail/product/id=91780', 'tags': 'USB C Type-C Receptacle SMD USB 2.0', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_C_Receptacle_JAE_DX07S016JA1R1500.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_USB : USB_C_Receptacle_JAE_DX07S016JA1R1500')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

