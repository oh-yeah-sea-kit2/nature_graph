# Nature Remoでデータ取得

## 概要
５分に１度、APIを叩いて部屋の温度変化をグラフとしてだす

## アクセストークンでアクセスできるか確認
curl -X GET "https://api.nature.global/1/devices" -H "accept: application/json" -k --header "Authorization: Bearer AccessTokens" | jq .


### ５分ごとにデータ取得のCRON
*/10 * * * * cd /home/user/workspace/private/nature_graph; . /home/user/.local/share/virtualenvs/nature_graph-vC8YyjG1/bin/activate;python main.py
