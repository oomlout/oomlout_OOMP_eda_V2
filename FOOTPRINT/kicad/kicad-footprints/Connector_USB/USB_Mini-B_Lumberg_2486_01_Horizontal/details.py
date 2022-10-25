
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_Mini-B_Lumberg_2486_01_Horizontal"
    hexID = "FZKCNUUMBLUMBERG24861HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_Mini-B_Lumberg_2486_01_Horizontal', 'description': 'USB Mini-B 5-pin SMD connector, http://downloads.lumberg.com/datenblaetter/en/2486_01.pdf', 'tags': 'USB USB_B USB_Mini connector', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_Mini-B_Lumberg_2486_01_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_USB : USB_Mini-B_Lumberg_2486_01_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

