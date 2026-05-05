"""Synthetic source connector for closed-loop discovery runs."""

from __future__ import annotations

import random
from typing import Any


MOCK_POSTS_BY_STRATEGY: dict[str, list[str]] = {
    "guaranteed_return_cluster": [
        "合成樣本：保證獲利的投資社群邀請，聲稱每天都有穩定收益並要求先私訊。",
        "合成樣本：保證收益課程，強調加入群組後會提供明牌與操作時間。",
        "合成樣本：穩賺投資方案，搭配收益截圖與限時名額說法。",
        "合成樣本：老師說本週保證翻倍，請留言領取投資社群資訊。",
        "合成樣本：宣稱零風險獲利，並引導使用者加入私人群組。",
        "合成樣本：高勝率股票策略，附收益見證並要求加 LINE 群。",
        "合成樣本：保本獲利話術，搭配助理回覆與社群導流。",
        "合成樣本：保證每天領現金流，留言後由分析師聯繫。",
    ],
    "authority_impersonation_cluster": [
        "合成樣本：投資老師帶單，助理會通知買賣點並邀請加入群組。",
        "合成樣本：自稱官方分析師，提供專屬股票健檢與私訊服務。",
        "合成樣本：名師助理整理飆股名單，限額開放社群會員。",
        "合成樣本：專家老師分享投資秘訣，留言後取得進階名單。",
        "合成樣本：分析師團隊聲稱可協助判斷持股並安排一對一諮詢。",
        "合成樣本：老師免費教學但要求先加入私人社群。",
        "合成樣本：助理代發收益案例，請讀者私訊領取操作表。",
    ],
    "off_platform_contact_cluster": [
        "合成樣本：文章要求加 LINE 群取得股票代碼與進出場提醒。",
        "合成樣本：留言區引導改用 Telegram 群討論投資標的。",
        "合成樣本：私訊我領取今日名單，加入社群後會有助理協助。",
        "合成樣本：加入 WhatsApp 投資群，宣稱可取得老師即時通知。",
        "合成樣本：投資社群招募，要求先 DM 再由助理安排入群。",
        "合成樣本：加群後提供保證收益策略與限時操作提醒。",
        "合成樣本：請留言想學，助理會私訊提供群組入口。",
    ],
    "urgency_teaser_cluster": [
        "合成樣本：限時名額倒數，今天不加入就錯過明牌。",
        "合成樣本：盤前最後提醒，私訊領取即將噴出的股票代碼。",
        "合成樣本：名額只剩十位，老師今晚公布操作策略。",
        "合成樣本：明天開盤前必看，加入群組才能取得完整名單。",
        "合成樣本：短線機會即將啟動，請立刻留言領取資訊。",
        "合成樣本：最後一次免費分享，助理會協助安排進群。",
    ],
    "hard_negative_calibration": [
        "合成樣本：一般投資心得，提醒不要相信保證獲利與陌生群組。",
        "合成樣本：市場討論文，說明投資風險並建議自行研究。",
        "合成樣本：反詐提醒，呼籲不要加入陌生 LINE 投資群。",
        "合成樣本：個人投資日記，記錄虧損與風險控管。",
        "合成樣本：金融教育內容，解釋ETF配置與長期風險。",
        "合成樣本：新聞評論，沒有邀請私訊或加入群組。",
    ],
}

STRATEGY_BY_SIGNAL = {
    "guaranteed_return": "guaranteed_return_cluster",
    "authority_impersonation": "authority_impersonation_cluster",
    "off_platform_contact": "off_platform_contact_cluster",
    "urgency": "urgency_teaser_cluster",
    "hard_negative_warning": "hard_negative_calibration",
}


def fetch_candidates(query: dict[str, Any]) -> list[dict[str, str]]:
    """Return 5-10 synthetic raw text items for one query object."""
    strategy = str(query.get("strategy") or "")
    if strategy not in MOCK_POSTS_BY_STRATEGY:
        strategy = STRATEGY_BY_SIGNAL.get(str(query.get("expected_signal") or ""), "hard_negative_calibration")
    posts = list(MOCK_POSTS_BY_STRATEGY.get(strategy, MOCK_POSTS_BY_STRATEGY["hard_negative_calibration"]))
    budget = max(5, min(10, int(query.get("budget", 5) or 5)))
    rng = random.Random(f"{query.get('query_id')}:{query.get('budget')}:{query.get('weight')}")
    rng.shuffle(posts)
    selected = posts[: min(budget, len(posts))]
    return [
        {
            "mock_item_id": f"{query['query_id']}_mock_{index:02d}",
            "query_id": str(query["query_id"]),
            "strategy": strategy,
            "raw_text": raw_text,
        }
        for index, raw_text in enumerate(selected, 1)
    ]
