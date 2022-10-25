
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "USB-C_Male_EdgeMnt_DX07P024MJ1R1500"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSUCMALEEDGEMNTDX7P24MJ1R15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB-C_Male_EdgeMnt_DX07P024MJ1R1500', 'description': 'http://www.jae.com/z-en/pdf_download_exec.cfm?param=MB-0301-2E_DX07_PLUG.pdf', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('digikey-footprints : USB-C_Male_EdgeMnt_DX07P024MJ1R1500')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

