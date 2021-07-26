from flask import Flask

# Flask 앱 서버 인스터스
app = Flask(__name__)

# url 패턴 - 라우터 설정


@app.route('/')
def index():
    return "<h1>hello<h1>"


# 메인 테스트
if __name__ == "__main__":
    app.run(debug=True)
