from ..app import app,render_template,request,re,Markup,plugins,session
# from ..plugins.whatcms import gwhatweb


@app.route('/index')
def index():
    return render_template('index.html')

#自定义
@app.route('/')
@app.route('/index0')
def index0():
    return render_template('index0.html')

@app.route('/fuckcms', methods=['get', 'post'])
def fuckcms():
    if request.method == 'POST':
        print("post,fuck")
    else:
        return render_template('fuckcms.html')

@app.route('/bugtest/jiechi/', methods=['get', 'post'])
def bugtest_jiechi():
    print("0 jiechi")
    if request.method == 'POST':
        print("jiechi")
        return render_template('./bugtest/jiechi.html', data="xxxxxx", title='CMS识别')
    else:
        return render_template('./bugtest/jiechi.html')

@app.route('/info/who_is/')
def info_who():
    return render_template('./info/who_is.html')

@app.route('/info/port_scan/')
def info_scan():
    return render_template('./info/port_scan.html')


@app.route('/info/hosts_scan/')
def info_hosts():
    return render_template('./info/hosts_scan.html')

@app.route('/info/web_ident/')
def info_web():
    return render_template('./info/web_ident.html')

@app.route('/info/domain_scan/')
def info_domain():
    return render_template('./info/domain_scan.html')

@app.route('/info/subdomain_scan/')
def info_subdomain():
    return render_template('./info/subdomain_scan.html')

@app.route('/info/web_ident/')
def info_web_ident():
    return render_template('./info/web_ident.html')

####
@app.route('/whatcms', methods=['get', 'post'])
def whatcms():
    if request.method == 'POST':
        url = request.form.get("url")
        if re.match(r'^https?:/{2}\w.+$', url):
            try:
                whatcmsresult = gwhatweb(url).whatweb()
                return render_template('whatcms.html', data=whatcmsresult, title='CMS识别')
            except:
                whatcmsresult = {'total': '', 'url': '', 'result': '', 'time': ''}
                return render_template('whatcms.html', data=whatcmsresult, title='CMS识别')
    else:
        return render_template('whatcms.html', title="CMS识别")


@app.route('/jsfuck')
def jsfuck():
    return render_template('jsfuck.html', title='jsfuck解密')


@app.route('/getdomain')
def getdomin():
    return render_template('getdomain.html', title='旁站/C段')


@app.route('/information')
def information_scan():
    return render_template('information.html', title='信息泄露', data=Markup(list(plugins.angelsword['informationpocdict'].keys())))


@app.route('/industrial')
def industrial_scan():
    return render_template('industrial.html', title='工控安全', data=Markup(list(plugins.angelsword['informationpocdict'].keys())))


@app.route('/hardware')
def hardware_scan():
    print("hardware")
    return render_template('hardware.html', title='物联网安全', data=Markup(list(plugins.angelsword['informationpocdict'].keys())))


@app.route('/system')
def system_scan():
    return render_template('system.html', title='system安全', data=Markup(list(plugins.angelsword['systempocdict'].keys())))


@app.route('/cms')
def cms_scan():
    return render_template('cms.html', title='cms安全检测', data=Markup(list(plugins.angelsword['cmspocdict'].keys())))


@app.route('/search')
def search():
    dicts={"cms": Markup(list(plugins.angelsword['cmspocdict'].keys())), "industrial": Markup(list(plugins.angelsword['industrialpocdict'].keys())), "hardware": Markup(list(plugins.angelsword['hardwarepocdict'].keys())),"information": Markup(list(plugins.angelsword['informationpocdict'].keys())),"system": Markup(list(plugins.angelsword['systempocdict'].keys()))}
    return render_template('/search.html', title='搜索',data=dicts)

@app.route('/test')
def websockettest():
    return render_template('websocket.html',title='websocket')

@app.route('/subdomain')
def subdomain():
    return render_template('subdomain.html',title='子域名获取')

# @app.route('/nmap')
# def nmap():
#     print("nmap")
#     return render_template('nmap.html',title='nmap扫描')

@app.route('/nmap',methods=['get', 'post'])
def nmap():
    print("app_namp");
    return render_template('nmap.html',title='nmap扫描')

    # target_json=getjson()
    # return jsonify({'data':requests.get("https://api.hackertarget.com/nmap/?q={target}".format(target=target_json['target'].replace("http:","").replace("https:","").replace("/",""))).text})


@app.route('/login',methods=['get','post'])
def login():
    if request.method == 'POST':
        pass
    else:
        return render_template('login.html',data={"type":1})

@app.route('/reg',methods=['get','post'])
def reg():
    if request.method == 'POST':
        username=request.form.get("username")
        password=request.form.get("password")
        User(username,password).commit()
        render_template("login.html",msg="注册成功",data={"type":1})
    else:
        return render_template('login.html',data={"type":0})

print("publicview")



