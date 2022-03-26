from fastapi import FastAPI

import contribution

async def get_ranking_border(pages):
    await pages.goto('http://game.granbluefantasy.jp/#event/teamraid060/ranking')

    total_record_list = await pages.querySelectorAll('.txt-total-record')

    evaluated_total_record_list = []
    for i, total_record in enumerate(total_record_list):
        total_record = await pages.evaluate('(total_record) => total_record.textContent', total_record)

        # 貢献度だけを抽出
        if i % 2 != 0:
            evaluated_total_record_list.append(total_record.strip())

    contribution.insert(evaluated_total_record_list)

app = FastAPI()

@app.get('/border')
def getBorderContribution():
    borderContibution = contribution.fetchAll()
    return borderContibution
