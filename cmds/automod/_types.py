# Sakura Auto Moderation Types

from typing import TypeAlias, TypedDict, Literal

Actions: TypeAlias = Literal["ban", "kick", "mute", "timeout", "none"]


class Setting(TypedDict, total=False):
    "設定関連の型。"

    adminrole: list[str]  # 管理者ロール
    modrole: list[str]  # モデレーターロール
    muterole: int  # ミュートされた人用ロール

    antiraid: Literal["on", "off"]  # レイド対策ONOFF
    raidaction: Actions  # レイドが起こった時のアクション
    raidactiontime: int | float | None  # レイドアクションまでの時間

    ch: list[int]  # 例外チャンネル一覧
    role: list[int]  # 例外ロール一覧

    ngword: list[str]  # NGワード一覧

    action: dict[str, Actions | str]  # ストライクポイントによるアクション
