
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PCBEdge"
    oIndex = "BUS_PCIexpress_x4"
    hexID = "FZKCNPCBEDGEBUSPCIEXPRESSX4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BUS_PCIexpress_x4', 'description': 'PCIexpress Bus Edge Connector x1 http://www.ritrontek.com/uploadfile/2016/1026/20161026105231124.pdf#page=70', 'tags': 'PCIe', 'attributeType': None, 'pins': {'type': 'connect', 'shape': 'rect'}})
    newPart['name'].append('Connector_PCBEdge : BUS_PCIexpress_x4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

