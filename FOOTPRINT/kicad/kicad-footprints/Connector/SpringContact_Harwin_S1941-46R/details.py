
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector"
    oIndex = "SpringContact_Harwin_S1941-46R"
    hexID = "FZKCNSPRINGCONTACTHARWINS194146R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SpringContact_Harwin_S1941-46R', 'description': '7.25mm SMT Multi-directional Spring Contact (T+R), https://cdn.harwin.com/pdfs/S1941R.pdf', 'tags': 'spring contact emi emc shield', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector.3dshapes/SpringContact_Harwin_S1941-46R.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector : SpringContact_Harwin_S1941-46R')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

