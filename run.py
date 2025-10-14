import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    print("🔒 脆弱なショッピングモール - ウェブセキュリティ演習サイト")
    
    # App Runner用のポート設定
    port = int(os.environ.get('PORT', 8000))
    
    # 本番環境では debug=False
    is_production = os.environ.get('AWS_REGION') is not None
    debug_mode = not is_production
    
    if is_production:
        print(f"🚀 本番環境で起動中... Port: {port}")
    else:
        print(f"🌐 開発環境で起動中... http://localhost:{port}")
    
    print("⚠️  このサイトは学習目的のみで使用してください")
    app.run(host='0.0.0.0', port=port, debug=debug_mode) 