
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PCBEdge"
    oIndex = "Samtec_MECF-05-0_-L-DV_2x05_P1.27mm_Polarized_Edge"
    hexID = "FZKCNPCBEDGESAMTECMECF5LDV2X5P127POLARIZEDEDGE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Samtec_MECF-05-0_-L-DV_2x05_P1.27mm_Polarized_Edge', 'description': 'Highspeed card edge connector for PCBs with 05 contacts (polarized)', 'tags': 'conn samtec card-edge high-speed', 'attributeType': None, 'pins': {'type': 'connect', 'shape': 'rect'}})
    newPart['name'].append('Connector_PCBEdge : Samtec_MECF-05-0_-L-DV_2x05_P1.27mm_Polarized_Edge')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

