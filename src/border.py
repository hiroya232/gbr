async def get_ranking_border(pages):
    await pages.goto('http://game.granbluefantasy.jp/#event/teamraid060/ranking')

    total_records = await pages.querySelectorAll('.txt-total-record')
    for total_record in total_records:
        total_record = await pages.evaluate('(total_record) => total_record.textContent', total_record)
        print(total_record)
