import os
import sys
from app import create_app

print("=== 脆弱なショッピングモール デバッグ情報 ===")
print(f"Python version: {sys.version}")
print(f"Working directory: {os.getcwd()}")
print(f"PORT env var: {os.environ.get('PORT', 'not set')}")
print(f"AWS_REGION env var: {os.environ.get('AWS_REGION', 'not set')}")
print(f"SUPABASE_URL env var: {os.environ.get('SUPABASE_URL', 'not set')}")

try:
    print("Creating Flask app...")
    app = create_app()
    print("Flask app created successfully!")
except Exception as e:
    print(f"Error creating Flask app: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

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
        print(f"🌐 開発環境で起動中... Port: {port}")
    
    print("⚠️  このサイトは学習目的のみで使用してください")
    
    try:
        app.run(host='0.0.0.0', port=port, debug=debug_mode)
    except Exception as e:
        print(f"Error starting Flask app: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1) 