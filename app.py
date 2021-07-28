from flask import Flask, render_template, request

# Flask 앱 서버 인스터스
app = Flask(__name__)

# url 패턴 - 라우터 설정


@app.route('/')
def hello():
    # get을 통한 전달받은 데이터를 확인
    return render_template('hello.html')


@app.route('/applyphoto')
def photo_apply():
    location = request.args.get("location")
    cleaness = request.args.get("clean")
    built_in = request.args.get("built")
    print(location, cleaness, built_in)
    # return render_template('apply.html')


@app.route('/apply')
def apply():
    return render_template('apply.html')


@app.route('/list')
def list():
    return render_template('list.html')


# 메인 테스트
if __name__ == "__main__":
    app.run(debug=True)
