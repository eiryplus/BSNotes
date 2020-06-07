# 譜面の仕様

## 構成ファイル

* info.dat
* 譜面データファイル
* オーディオファイル(説明省略)

### info.dat

JSON形式で曲の情報が記載されている。

#### 重要な情報

| パラメータ名 | 意味 | 設定値のサンプル |
| --- | --- | ---|
| _beatsPerMinute | この設定値 == 1分 | 200 |
| _songFilename | オーディオファイル。おそらくVorbis形式 | With.ogg |
| _difficultyBeatmapSets.X._difficultyBeatmaps.X._difficulty | 難易度 | Hard / Expart / ExpertPlus |
| _difficultyBeatmapSets.X._difficultyBeatmaps.X._beatmapFilename | 譜面ファイル名 | Hard.dat |
| _difficultyBeatmapSets.X._difficultyBeatmaps.X._noteJumpMovementSpeed | 速さ | 18 |

### 譜面データファイル

JSON形式で譜面データが格納されている。

#### 重要な情報

| パラメータ名 | 意味 | 設定値のサンプル |
| --- | --- | ---|
| _notes | 全ノーツ情報のエレメント |  |
| _notes.X._time | タイミング。実際の時間ではなく info.datの _beatsPerMinute で変換された時間が設定されている | 6.6333332061767578 |
| _notes.X._lineIndex | 左右の位置。4レーンの場合、0が一番左、3が一番右 | 0 |
| _notes.X._lineLayer | 上下の位置。0が下段、2が上段。 | 0 |
| _notes.X.type | 0が左手で切るノーツ、1が右手で切るノーツ | 0 |
| _notes.X._cutDirection | 切る方向<br>・0: 上<br>・1: 下<br>・2: 左<br>・3: 右<br>・4: 左上<br>・5: 右上<br>・6: 左下<br>・7: 右下<br>・8: 全方向可 | 0 |
