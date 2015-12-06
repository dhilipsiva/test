import json

with open("vulnerabilities.json", "r") as f:
    vulnerabilities = "id,name\n"
    for vulnerability in json.loads(f.read()):
        vulnerabilities += '%(id)s,%(name)s\n' % vulnerability
    with open("vulnerabilities.csv", 'w') as csv:
        csv.write(vulnerabilities)


with open("research.json", "r") as f:
    apps = "id,category,version_string,apk_url,title,version_code,app_id,developer_name,packages\n"
    analyses = "id,file,vulnerability,risk\n"
    for app in json.loads(f.read()):
        app["packages"] = ",".join(app["packages"])
        apps += '%(id)s,%(category)s,"%(version_string)s",%(apk_url)s,"%(title)s",%(version_code)s,%(app_id)s,"%(developer_name)s","%(packages)s"\n' % app
        for analysis in app["analyses"]:
            analyses += "%(id)s,%(file)s,%(vulnerability)s,%(risk)s\n" % analysis
    with open("apps.csv", 'w') as csv:
        csv.write(apps)
    with open("analyses.csv", 'w') as csv:
        csv.write(analyses)
