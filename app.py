import os
from app import create_app

# Amplifyでの実行用エントリーポイント
app = create_app()

# 本番環境での設定
if os.environ.get('AWS_REGION'):
    app.config['DEBUG'] = False
    print("🚀 Running in AWS Amplify production environment")
else:
    print("🔧 Running in development environment")

# WSGIアプリケーションオブジェクトをエクスポート
application = app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)