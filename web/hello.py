from bottle import route, template


@route('/hello/<name:re:[abcde].*>')
@route('/hello')
@route('/hello/')
def hello(name='jarkko'):
    return template('<b>Hello {{name}}</b>!', name=name)


