def w3c_client(src):
    from json import loads
    import urllib
    msg=''
    res_json=''

    url = 'http://validator.w3.org/check'
    values = {'fragment' : src,'output':'json'}
    params = urllib.parse.urlencode(values)
    params=params.encode('utf-8')
    response=''
    req = urllib.request.Request(url, headers={},data=params)
    try:
        response = urllib.request.urlopen(req,timeout=10)
    except:
        print('URLError: Do you have an active Internet Connection?')

    if response:
        res_json = loads(response.read().decode())
        valid = response.info()['X-W3C-Validator-Status']
        if valid == "Valid":
            valid = True
        else:
            valid = False
        if not valid:
            warnings = int(response.info()['X-W3C-Validator-Warnings'])
            errors = int(response.info()['X-W3C-Validator-Errors'])
            msg="Valid markup: %s (Errors: %i, Warnings: %i) " % (valid, errors, warnings)
        return(valid,msg,res_json)


#Google Page-Speed, only when site is online and public
