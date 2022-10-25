
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_C_Plug_JAE_DX07P024AJ1"
    hexID = "FZKCNUUCPLUGJAEDX7P24AJ1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_C_Plug_JAE_DX07P024AJ1', 'description': 'Universal Serial Bus (USB) Shielded I/O Plug, Type C, Right Angle, Surface Mount, https://www.jae.com/en/searchfilter/?topics_keyword=DX07P024AJ1&mainItemSelect=1', 'tags': 'USB Type-C Plug Edge Mount', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_C_Plug_JAE_DX07P024AJ1.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_USB : USB_C_Plug_JAE_DX07P024AJ1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

