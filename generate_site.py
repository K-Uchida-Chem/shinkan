import os

# --- 設定：ここを書き換えるとサイトの内容が変わります ---
CONFIG = {
    "page_title": "北海道大学ボート部 新歓2025",
    "main_copy": "大学から全国へ",
    "theme_color": "#FFFFF0",  # アイボリー
    "text_color": "#1A1A1A",   # 読みやすい濃いグレー
    "accent_color": "#002F6C", # 北大らしい濃い青（リンクやボタン用）
    "instagram_url": "https://www.instagram.com/hurc2025?igsh=aWQ4a3dwOWRoc203",
    "concept_text": """
    なぜ、私たちは早朝の寒さの中でオールを握るのか。
    それは「勝利」という一瞬の熱狂を知っているからだ。
    理屈じゃない。
    ただ、日本一速い艇を進める。
    そのシンプルな目標に、大学生活のすべてを賭ける価値がある。
    """,
    "captain_message": """
    【主将メッセージ】
    北大ボート部は、本気で日本一を目指す集団です。
    経験は問いません。必要なのは「熱意」だけ。
    君の4年間を、私たちに預けてみませんか。
    一緒に、見たことのない景色を見に行きましょう。
    """,
    "schedule_info": """
    【試乗会・説明会日程】
    4月の土日祝日に開催予定。
    詳細はInstagramにて随時更新中。
    """,
}

# --- HTMLテンプレート生成関数 ---
def generate_html(config):
    html_content = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{config['page_title']}</title>
    <style>
        /* 軽量化のためCSSは内部に記述 */
        body {{
            font-family: "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Hiragino Sans", Meiryo, sans-serif;
            background-color: {config['theme_color']};
            color: {config['text_color']};
            margin: 0;
            padding: 0;
            line-height: 1.8;
            letter-spacing: 0.05em;
        }}
        .container {{
            max_width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        /* ヒーローセクション */
        .hero {{
            height: 80vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            /* 背景画像を設定する場合はここに url('path/to/image.jpg') を追加 */
            background-image: url('hero_bg.jpg');
            background-size: cover;
            background-position: center;
            color: #fff;
            text-shadow: 0 2px 4px rgba(0,0,0,0.8);
        }}
        .hero h1 {{
            font-size: 3.5rem;
            font-weight: 900;
            margin: 0;
            border-bottom: 4px solid #fff;
            padding-bottom: 10px;
        }}
        
        /* 各セクション */
        section {{
            margin: 80px 0;
        }}
        h2 {{
            font-size: 1.5rem;
            border-left: 5px solid {config['text_color']};
            padding-left: 15px;
            margin-bottom: 30px;
        }}
        p {{
            font-size: 1.1rem;
            white-space: pre-line; /* 改行を反映 */
        }}

        /* YouTube埋め込みレスポンシブ対応 */
        .video-container {{
            position: relative;
            padding-bottom: 56.25%;
            height: 0;
            overflow: hidden;
            background: #000;
        }}
        .video-container iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }}

        /* CTAボタン */
        .cta-button {{
            display: inline-block;
            background-color: {config['accent_color']};
            color: #fff;
            padding: 20px 40px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.2rem;
            border-radius: 5px;
            transition: opacity 0.3s;
        }}
        .cta-button:hover {{
            opacity: 0.8;
        }}
        .center-text {{
            text-align: center;
        }}
        footer {{
            text-align: center;
            padding: 40px;
            font-size: 0.8rem;
            opacity: 0.7;
        }}
        
        /* Recruitment Section Background */
        #info {{
            background-image: url('recruitment_bg.jpg');
            background-size: cover;
            background-position: center;
            padding: 60px 20px;
            color: #fff; /* 文字色を白に */
            text-shadow: 0 2px 4px rgba(0,0,0,0.8); /* 文字の可読性を高める */
            border-radius: 10px;
        }}
        #info h2 {{
            border-left-color: #fff; /* 見出しのボーダーも白に */
        }}
        
        /* スマホ向け調整 */
        @media (max-width: 600px) {{
            .hero h1 {{ font-size: 2rem; }}
            .container {{ padding: 15px; }}
            section {{ margin: 50px 0; }}
        }}
    </style>
</head>
<body>

    <div class="hero">
        <h1>{config['main_copy']}</h1>
    </div>

    <div class="container">
        
        <section id="concept">
            <h2>CONCEPT</h2>
            <p>{config['concept_text']}</p>
        </section>

        <section id="message">
            <h2>CAPTAIN'S MESSAGE</h2>
            <p>{config['captain_message']}</p>
        </section>

        <section id="movie">
            <h2>PROMOTION VIDEO</h2>
            <div class="video-container">
                <iframe 
                    width="560" 
                    height="315" 
                    src="https://www.youtube.com/embed/2pcHALaBtZs" 
                    title="YouTube video player" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                    referrerpolicy="strict-origin-when-cross-origin" 
                    allowfullscreen>
                </iframe>
            </div>
        </section>

        <section id="info">
            <h2>RECRUITMENT</h2>
            <p>{config['schedule_info']}</p>
            
            <div class="center-text" style="margin-top: 50px;">
                <p>最新情報はInstagramでチェック</p>
                <a href="{config['instagram_url']}" class="cta-button" target="_blank">Instagramを見る</a>
            </div>
        </section>

    </div>

    <footer>
        <p>© 2025 Hokkaido University Rowing Club</p>
    </footer>

</body>
</html>
    """
    return html_content

# --- 実行部分 ---
if __name__ == "__main__":
    html = generate_html(CONFIG)
    output_file = "index.html"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"✅ 生成完了: {output_file}")
    print("このファイルをブラウザで開いて確認してください。")
