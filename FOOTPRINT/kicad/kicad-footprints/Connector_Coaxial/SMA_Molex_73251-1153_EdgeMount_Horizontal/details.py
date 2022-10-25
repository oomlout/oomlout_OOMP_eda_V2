
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Coaxial"
    oIndex = "SMA_Molex_73251-1153_EdgeMount_Horizontal"
    hexID = "FZKCNCOASMX732511153EDGEMOUNTHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SMA_Molex_73251-1153_EdgeMount_Horizontal', 'description': 'Molex SMA RF Connectors, Edge Mount, (http://www.molex.com/pdm_docs/sd/732511150_sd.pdf)', 'tags': 'sma edge', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Coaxial.3dshapes/SMA_Molex_73251-1153_EdgeMount_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Coaxial : SMA_Molex_73251-1153_EdgeMount_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

