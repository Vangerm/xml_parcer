from aiogram.types import Message
import xml.etree.ElementTree as ET
import csv


@dp.message()
async def send_done_xml(message: Message):
    await message.answer(text=message.chat.id)


def indent(elem, level: int = 0) -> None:
    '''создает красивый xml c отступами'''
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def csv_dict() -> dict:
    result = {}
    with open('input.csv', encoding='utf-8') as f:
        csv_file = csv.DictReader(f, delimiter=',')
        for item in csv_file:
            result.setdefault(item['set'], []).append(item['code'])
    return result


def app_cis(elem) -> None:
    for set, codes in csv_dict().items():
        pack_content_item = ET.Element('pack_content')
        pack_code_item = ET.Element('pack_code')

        elem[0].append(pack_content_item)

        pack_code_item.text = set
        elem[0][-1].append(pack_code_item)

        for code in codes:
            cis_item = ET.Element('cis')
            cis_item.text = code
            elem[0][-1].append(cis_item)


def start():
    tree = ET.parse('Формирование_наборов.xml')
    root = tree.getroot()

    app_cis(root)

    indent(root)
    tree.write('output.xml', encoding="utf-8", xml_declaration=True)
