
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PCBEdge"
    oIndex = "Samtec_MECF-60-01-L-DV-WT_2x60_P1.27mm_Polarized_Socket_Horizontal"
    hexID = "FZKCNPCBEDGESAMTECMECF61LDVWT2X6P127POLARIZEDSOHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Samtec_MECF-60-01-L-DV-WT_2x60_P1.27mm_Polarized_Socket_Horizontal', 'description': 'Highspeed card edge connector for 1.6mm PCBs with 60 contacts (polarized)', 'tags': 'conn samtec card-edge high-speed', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PCBEdge.3dshapes/Samtec_MECF-60-01-L-DV-WT_2x60_P1.27mm_Polarized_Socket_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_PCBEdge : Samtec_MECF-60-01-L-DV-WT_2x60_P1.27mm_Polarized_Socket_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

